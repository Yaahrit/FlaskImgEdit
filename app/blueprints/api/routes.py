from flask import Blueprint, jsonify, request
from app.services.image_service import ImageService

api_bp = Blueprint('api', __name__)

@api_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online", "version": "1.0.0"})

@api_bp.route('/process', methods=['POST'])
def api_process():
    # Placeholder for API-based processing
    # In a real app, this would handle base64 or multipart uploads
    return jsonify({"message": "API endpoint for processing is under construction"}), 501
