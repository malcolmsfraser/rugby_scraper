install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt

test:
	pass
	
lint:
	pylint --disable=R,C super_rugby/super_rugby/settings.py
		pylint --disable=R,C,W0221 super_rugby/super_rugby/spiders/rugbyspider.py
	
	
all: install lint test
