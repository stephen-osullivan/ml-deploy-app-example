# ml-deploy-app-example
Here we do some EDA and fit some models to the famous breast cancer dataset. Once this is done we convert our model into an app using flask.

exploratory-data-analysis.ipynb shows how the model and data were created.
app.py contains the flask application code

To run the endpoint:
1. Create a virtual environment and load the requirements.txt file
2. Create the endpoint with: $ python app.py
3. Send the predictions in the sample_predictions.json to the endpoint with:$ curl -X POST -H "Content-Type: application/json" -d @sample_predictions.json http://127.0.0.1:5000/predict
