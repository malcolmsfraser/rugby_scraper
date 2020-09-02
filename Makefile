install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt

test:
	python -m pytest -vv settings.py
	python -m pytest -vv rugbyspider.py
	
lint:
	pylint --disable=R,C settings.py
	pylint --disable=R,C rugbyspider.py
	
	
all: install lint test