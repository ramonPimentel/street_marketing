run:
	uvicorn main:app --reload --host=0.0.0.0 --port 9000

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f .coverage.NB-SBDEV*
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

coverage: clean
	@py.test --cov=app --cov-report=term-missing --cov-report=xml --cov-fail-under=80 ./tests/