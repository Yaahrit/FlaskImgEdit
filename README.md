# EditMonkey - Professional Image Editor

EditMonkey is a production-ready Flask application designed for fast and secure image processing using OpenCV.

## Features

- **Modular Architecture**: Built with Flask Blueprints and an App Factory pattern.
- **Advanced Processing**: Support for Grayscale, Gaussian Blur, Rotation, Edge Detection, and Brightness/Contrast adjustments.
- **Premium UI**: Modern dashboard using Tailwind CSS and DaisyUI.
- **Interactive Experience**: Drag-and-drop uploads, live previews, and sleek animations.
- **Security**: UUID-based filename sanitization, strict file validation, and secure storage.
- **Developer Ready**: Includes REST API placeholders and automated unit tests.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Create a `.env` file (one has been provided for you).

3. **Run the Application**:
   ```bash
   python wsgi.py
   ```
   Or using Gunicorn:
   ```bash
   gunicorn wsgi:app
   ```

4. **Run Tests**:
   ```bash
   python -m unittest discover tests
   ```

## Project Structure

- `app/`: Main application package
  - `blueprints/`: Modular route handlers
  - `services/`: Business logic (OpenCV)
  - `static/`: CSS, JS, and image storage
  - `templates/`: HTML templates
- `tests/`: Automated test suite
- `config.py`: Environment-based configuration
- `wsgi.py`: Production entry point

## License
MIT
