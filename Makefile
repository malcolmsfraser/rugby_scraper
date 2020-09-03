install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_total_points.py
	
lint:
	pylint --disable=R,C super_rugby/super_rugby/settings.py
		pylint --disable=R,C,W0221 super_rugby/super_rugby/spiders/2020rugbyspider.py
			pylint --disable=R,C,no-value-for-parameter total_points.py
				pylint --disable=R,C test_total_points.py
	
	
all: install lint test
