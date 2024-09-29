from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

# Load the model once when the app starts
model = load_model('horseWinPredictor.h5')

@app.route('/')
def index():
    return send_from_directory('.', 'betting.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read the CSV file from the request
    file = request.files['file']
    data = pd.read_csv(file)
    
    # Ensure the data is in the correct format for the model
    # Assuming the model expects a specific set of features
    # Adjust the following line according to your model's requirements
    features = data[['win', 'podium', 'place']]  # Replace with actual feature names
    
    # Make predictions
    predictions = model.predict(features)
    
    # Convert predictions to a list and return as JSON
    return jsonify(predictions=predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
