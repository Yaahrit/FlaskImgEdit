# 🖼️ FlaskImgEdit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  A lightweight browser-based image editing web application built with <strong>Flask</strong> and <strong>OpenCV</strong>.
  Upload, process, and transform images directly from your browser — no software installation required.
</p>

---

## ✨ Features

- 📤 **Image Upload** — Upload images via a clean web interface
- 🔧 **OpenCV Processing** — Apply image operations powered by OpenCV
- 🌐 **Browser-Based** — No desktop app needed; runs fully in the browser
- 🔌 **Easily Extendable** — Add filters, face detection, resizing, and more with minimal effort

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Image Processing | OpenCV (`cv2`) |
| Frontend | HTML5, CSS3 |
| Server | Flask Development Server |

---

## 📁 Project Structure

```
FlaskImgEdit/
│
├── main.py               # Core Flask application & route handlers
├── static/               # Static assets (CSS, JS, processed images)
└── templates/
    └── index.html        # Main UI template
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yaahrit/FlaskImgEdit.git
cd FlaskImgEdit

# 2. Install dependencies
pip install flask opencv-python

# 3. Create required directories
mkdir static templates

# 4. Run the application
python main.py
```

### Access the App

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📌 Usage

1. Open the app in your browser
2. Upload an image (`.jpg`, `.png`, `.jpeg` supported)
3. Select the desired image operation
4. View and download the processed image

---

## 🚀 Planned Enhancements

- [ ] Grayscale & color filter options
- [ ] Image resizing and cropping
- [ ] Edge detection using Canny algorithm
- [ ] Face detection using Haar Cascades
- [ ] Brightness & contrast control
- [ ] Download processed image button

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Yash Raj**
[![Portfolio](https://img.shields.io/badge/Portfolio-FF6B00?style=flat&logo=vercel&logoColor=white)](https://yashrajhub.netlify.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/yashrajhub)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/yaahrit)

---

<p align="center">⭐ If you found this helpful, consider starring the repo!</p>
