import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from app.services.image_service import ImageService
import uuid

editor_bp = Blueprint('editor', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@editor_bp.route('/')
def dashboard():
    return render_template('editor/index.html')

@editor_bp.route('/batch')
def batch():
    return render_template('editor/batch.html')

@editor_bp.route('/filters')
def filters():
    return render_template('editor/filters.html')

@editor_bp.route('/batch_upload', methods=['POST'])
def batch_upload():
    if 'files[]' not in request.files:
        return jsonify({"error": "No files"}), 400
    
    files = request.files.getlist('files[]')
    width = int(request.form.get('width', 800))
    height = int(request.form.get('height', 600))
    
    processed_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_filename = f"batch_{uuid.uuid4().hex}_{filename}"
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
            
            # Simple resize for batch
            processed = ImageService.process(unique_filename, 'resize', {'width': width, 'height': height})
            processed_files.append(processed)
            
    return jsonify({"success": True, "processed": processed_files})

@editor_bp.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Unique filename to prevent collisions
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
        
        return render_template('editor/index.html', filename=unique_filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, webp, gif', 'error')
        return redirect(request.url)

@editor_bp.route('/process', methods=['POST'])
def process():
    filename = request.form.get('filename')
    operation = request.form.get('operation')
    
    if not filename or not operation:
        flash('Missing parameters', 'error')
        return redirect(url_for('editor.dashboard'))

    # Extract params from form
    params = request.form.to_dict()
    
    try:
        processed_filename = ImageService.process(filename, operation, params)
        return render_template('editor/index.html', 
                               original=filename, 
                               processed=processed_filename,
                               operation=operation)
    except Exception as e:
        current_app.logger.error(f"Processing error: {str(e)}")
        flash(f"Error processing image: {str(e)}", 'error')
        return render_template('editor/index.html', filename=filename)

@editor_bp.route('/download/<filename>')
def download(filename):
    return send_from_directory(current_app.config['PROCESSED_FOLDER'], filename, as_attachment=True)
