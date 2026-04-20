import os
import logging
from flask import Flask
from config import config_by_name

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Setup logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    # Ensure upload and processed folders exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

    # Register Blueprints
    from app.blueprints.main.routes import main_bp
    from app.blueprints.editor.routes import editor_bp
    from app.blueprints.api.routes import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(editor_bp, url_prefix='/editor')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
