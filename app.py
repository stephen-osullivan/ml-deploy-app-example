# simple endpoint app
from flask import Flask, request, jsonify
from joblib import load
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


model = load('model.joblib')
app = Flask(__name__)
@app.route('/')
def home():
    return "Breast Cancer Predictions"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = pd.DataFrame.from_dict(request.get_json())

    # Make predictions with the model
    pred = model.predict(data)

    # Return the predictions as a JSON response
    return jsonify({'prediction': list(pred)})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)