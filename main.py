import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
app.secret_key = 'super secret key'


# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']


def processImage(filename, operation):
    print(f"The operation is {operation} and filename {filename} is ")
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgray":
            imgProcess = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"static/{filename}"
            cv2.imwrite(newFilename, imgProcess)
            return newFilename
        case "cpng":
            newFilename = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cwebp":
            newFilename = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cjpg":
            newFilename = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img)
            return newFilename

    pass


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get('operation')
        # Check if the file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return "Error: No file part"
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Error : No file selected"

        # Check if the file has an allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = processImage(filename, operation)
            flash(
                f"Your image has been processed and is available <a href='/{new}' target='_blank'>Here</a>.")
            return render_template("index.html")
        else:
            flash('Invalid file type')
            return "Error : Invalid file type"
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
