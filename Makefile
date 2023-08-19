init:
	pip install -r requirements.txt

unit_tests:
	python -m pytest -v -m unit

unit_tests_log:
	python -m pytest --log-cli-level=INFO -v -m unit

