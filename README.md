# ml-deploy-app-example
Here we do some EDA and fit some models to the famous breast cancer dataset. Once this is done we convert our model into an app using flask and demonstrate a full CICD pipeline that automatically tests our app and then deploys it to azure app services as a live website.

A great free web book for implementing MLOPS principles is: [pragmatic ai labs](https://paiml.com/docs/home/books/cloud-computing-for-data/)

## What is MLOPS?
MLOPS is about implementing proven and effective DEVOPS principles in machine learning projects. The main concepts behind DEVOPS are CI (Continuous Integration) and CD (Continuous Delivery):
1. Continuous Integration (CI): Whenever a push to main is made, github actions automatically installs a venv with the requirements.txt file and then lints and tests the code.
2. Continuous Delivery (CD): If the tests/linting pass, then the repo automatically pushes the new version of the app to azure and deploys it in real time.

Setting up these two elements saves a lot of time in the long run, avoids headaches and leaves to painless updates and iteration to your project.

## Example MLOPS Project
Here is what a standard lightweight ML pipeline looks like:

![example pipeline](https://user-images.githubusercontent.com/58792/85235537-c149aa80-b3e3-11ea-8252-60e42157d75c.jpg)

The one we implement in this project is almost identical, but using github actions to deploy rather than azure pipelines.

This project is very flexible however, and it would be no extra effort to deploy to AWS (e.g elastic beanstalk) or GCP (cloud run/ app engine).

## This Project

Files:

* exploratory-data-analysis.ipynb shows how the model and data were created.
* model.joblib contains the model train in the .ipynb notebook
* app.py contains the flask application code
* requirements_development.txt contains the requirements necessary to run the notebook and train the model.
* requirements.txt is more lightweight and contains just the requirements necessary to deploy the model to the app.
* .github directory contains the github actions CICD actions. 

To run the endpoint locally:

1. Create a virtual environment and load the requirements.txt file using $ make install
2. Create the endpoint with: $ make deploy
3. Send the predictions in the sample_predictions.json to the endpoint with:$ curl -X POST -H "Content-Type: application/json" -d @sample_predictions.json http://127.0.0.1:5000/predict

