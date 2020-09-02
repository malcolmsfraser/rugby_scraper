install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt

test:
	pass
	
lint:
	pylint --disable=R,C settings.py
	pylint --disable=R,C rugbyspider.py
	
	
all: install lint test
