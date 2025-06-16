import io
from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
from torchvision import models

app = Flask(__name__)

weights = models.MobileNet_V2_Weights.DEFAULT
model = models.mobilenet_v2(weights=weights)
model.eval()
preprocess = weights.transforms()
class_names = weights.meta["categories"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'}), 400
    file = request.files['image']
    image = Image.open(file.stream).convert('RGB')
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence, pred_idx = torch.max(probabilities, dim=0)
    return jsonify({'label': class_names[pred_idx], 'confidence': float(confidence)})

if __name__ == '__main__':
    app.run(debug=True)
