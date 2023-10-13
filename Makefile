install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

test:
	python -m pytest -vv

launch-app:
	python app.py

sample-predict:
	curl -X POST -H "Content-Type: application/json" -d @sample_predictions.json http://127.0.0.1:5000/predict

az-deploy-app:
	az webapp up --runtime PYTHON:3.8 --sku B1 --location uksouth --plan sostestapp
	
all: install lint test