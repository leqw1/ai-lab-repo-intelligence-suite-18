test:
	python -m unittest discover -s tests

build:
	python -m compileall app scripts tests

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000
