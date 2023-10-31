# simple endpoint app
from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

def load_model():
    model = load('model.joblib')
    return model

app = Flask(__name__)

@app.route('/')
def home():
    return "Breast Cancer Predictions. Use /predict for predictions."

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = pd.DataFrame.from_dict(request.get_json())

    # Make predictions with the model
    model = load_model()
    pred = model.predict(data)

    # Return the predictions as a JSON response
    return jsonify({'prediction': list(pred)})

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)