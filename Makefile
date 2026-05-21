.PHONY: install generate-data generate-tasks generate-scenarios run-pipeline test lint format dashboard api docker-up docker-down

install:
	python -m pip install -r requirements.txt

generate-data:
	python -m src.data_generation.generate_domain_data

generate-tasks:
	python -m src.data_generation.generate_tasks

generate-scenarios:
	python -m src.data_generation.generate_probability_scenarios

run-pipeline:
	python -m src.pipeline.run_all

test:
	python -m pytest

lint:
	python -m ruff check .

format:
	python -m ruff format .

dashboard:
	streamlit run src/dashboard/app.py

api:
	uvicorn src.api.main:app --reload

docker-up:
	docker compose up --build

docker-down:
	docker compose down

