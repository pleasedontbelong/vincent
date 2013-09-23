flake8:
	flake8 vincent

test:
	coverage run --branch --source=vincent manage.py test ${app} -s -x --settings=vincent.settings.test

test-report:
	coverage report --include="*/apps/*" --omit="*__init__*","*tests*"

test-html:
	coverage html --include="*/apps/*" --omit="*__init__*","*tests*"
	firefox "file://$(CURDIR)/htmlcov/index.html" &