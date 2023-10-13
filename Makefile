install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

launch:
	python app.py

sample-predict:
	curl -X POST -H "Content-Type: application/json" -d @sample_predictions.json http://127.0.0.1:5000/predict

all: install lint