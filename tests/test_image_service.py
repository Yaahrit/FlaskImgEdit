import unittest
import os
import cv2
import numpy as np
from app import create_app
from app.services.image_service import ImageService

class TestImageService(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        # Create test upload folder
        os.makedirs(self.app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(self.app.config['PROCESSED_FOLDER'], exist_ok=True)
        
        # Create a dummy image
        self.test_filename = "test_image.jpg"
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(os.path.join(self.app.config['UPLOAD_FOLDER'], self.test_filename), img)

    def tearDown(self):
        self.app_context.pop()
        # Cleanup could be added here

    def test_grayscale(self):
        processed = ImageService.process(self.test_filename, 'grayscale')
        self.assertTrue(os.path.exists(os.path.join(self.app.config['PROCESSED_FOLDER'], processed)))
        img = cv2.imread(os.path.join(self.app.config['PROCESSED_FOLDER'], processed))
        self.assertEqual(len(img.shape), 2) # Grayscale should have 2 dims (or check channels)
        # Note: cv2.imread might read grayscale as 3-channel if not specified, 
        # but let's check if the file exists and is readable.

    def test_rotate(self):
        processed = ImageService.process(self.test_filename, 'rotate', {'angle': 90})
        self.assertTrue(os.path.exists(os.path.join(self.app.config['PROCESSED_FOLDER'], processed)))

if __name__ == '__main__':
    unittest.main()
