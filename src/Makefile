SHELL=bash

node-init:
	@npm install

serverless-init:
	@npm install -g serverless

create-venv:
	@python -m venv venv

activate-venv:
	 source ./venv/bin/activate && pip install -r requirements.txt

deploy-data-ingestion:
	cd data-ingestion-service && serverless deploy
