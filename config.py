import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-very-secret'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'uploads')
    PROCESSED_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'processed')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'tests', 'uploads')

class ProductionConfig(Config):
    # Production specific configs
    pass

config_by_name = {
    'dev': DevelopmentConfig,
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
