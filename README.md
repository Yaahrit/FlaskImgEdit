📸 FlaskImgEdit
A simple web application built with Flask and OpenCV that allows you to edit images directly in your browser.

🚀 Features
Upload and view images via a web interface

Perform basic image operations using OpenCV

Easily extendable for more advanced image editing tasks

🧰 Requirements
Make sure you have Python installed. Then install the required packages:

pip install flask opencv-python
📁 Project Structure
FlaskImgEdit/
│
├── main.py               # Main Flask application
├── static/               # Folder to store static assets (CSS, JS, images)
└── templates/
    └── index.html        # Main HTML page for UI
📝 Setup Instructions
Clone the repository or create a new project folder

Install dependencies

pip install flask opencv-python
Create the required folders

mkdir static templates
Create files

In the root: main.py

In the templates/ folder: index.html

Run the Flask app

python main.py
Access the app
Open your browser and go to: http://127.0.0.1:5000

📌 Notes
Make sure the image files are saved in a supported format (e.g., .jpg, .png).

You can extend this project by adding filters, resizing options, face detection, etc.

📷 Screenshot (Optional)
Add a screenshot of your application here for better presentation.

🤝 Contribution
Feel free to fork this repository and enhance the functionality. Pull requests are welcome!

📄 License
This project is open-source and available under the MIT License.
