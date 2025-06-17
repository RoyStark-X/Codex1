# Image Recognition Demo

This project demonstrates a simple web application for classifying images using TensorFlow.js and MobileNet.
Uploaded pictures are displayed on the page and the top predictions are shown
in a neat table with their confidence levels.

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
4. Open `http://localhost:5000` in your browser. Upload an image to see it displayed on the page along with the top predictions and their confidence levels.

The classification runs entirely in the browser using a pre-trained MobileNet model.

