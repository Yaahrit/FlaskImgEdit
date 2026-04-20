import cv2
import numpy as np
import os
import uuid
from flask import current_app

class ImageService:
    @staticmethod
    def _get_path(filename, folder='uploads'):
        if folder == 'uploads':
            return os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        return os.path.join(current_app.config['PROCESSED_FOLDER'], filename)

    @staticmethod
    def _generate_filename(original_filename, suffix=''):
        ext = original_filename.rsplit('.', 1)[1].lower()
        return f"{uuid.uuid4().hex}{suffix}.{ext}"

    @classmethod
    def process(cls, filename, operation, params=None):
        input_path = cls._get_path(filename, 'uploads')
        img = cv2.imread(input_path)
        
        if img is None:
            raise ValueError("Could not read image")

        output_img = img
        suffix = f"_{operation}"

        if operation == 'grayscale':
            output_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        elif operation == 'blur':
            ksize = int(params.get('ksize', 5))
            if ksize % 2 == 0: ksize += 1
            output_img = cv2.GaussianBlur(img, (ksize, ksize), 0)
        
        elif operation == 'rotate':
            angle = int(params.get('angle', 90))
            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            output_img = cv2.warpAffine(img, M, (w, h))
        
        elif operation == 'resize':
            width = int(params.get('width', 300))
            height = int(params.get('height', 300))
            output_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        
        elif operation == 'edges':
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            output_img = cv2.Canny(gray, 100, 200)
        
        elif operation == 'brightness':
            alpha = float(params.get('contrast', 1.0)) # Contrast control (1.0-3.0)
            beta = int(params.get('brightness', 0))    # Brightness control (0-100)
            output_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

        output_filename = cls._generate_filename(filename, suffix)
        output_path = cls._get_path(output_filename, 'processed')
        
        cv2.imwrite(output_path, output_img)
        return output_filename
