from flask import Flask, request, jsonify
import pandas as pd
from tensorflow.keras.models import load_model


app = Flask(__name__)

# Load the model once when the app starts
model = load_model('horseWinPredictor.h5')

@app.route('/predict', methods=['POST'])
def predict():
	# Read the CSV file from the request
	file = request.files['file']
	data = pd.read_csv(file)
	
	# Make predictions
	predictions = model.predict(data)
	
	# Convert predictions to a list and return as JSON
	return jsonify(predictions.tolist())

if __name__ == '__main__':
	app.run(debug=True)

data = pd.read_csv('testCases.csv')
print(model.predict(data))