# Image Recognition Demo

This project demonstrates a simple web application for classifying images using TensorFlow.js and MobileNet.

## Usage

1. Ensure Python and `flask` are installed.
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Start the server:
   ```bash
   python app.py
   ```
4. Open `http://localhost:5000` in your browser, upload an image and see the predictions with confidence levels.

The classification runs entirely in the browser using a pre-trained MobileNet model.
