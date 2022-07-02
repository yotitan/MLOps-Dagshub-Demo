setup:
	python3 -m venv ~/.MLOps-Dagshub-Demo
	source ~/.MLOps-Dagshub-Demo/bin/activate
	
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	
test:
	python3 -m pytest -vv -cov=$(git ls-files '*_test.py')
	
lint:
	pylint --disable R,C *.py
	
all:
	make test
	make lint