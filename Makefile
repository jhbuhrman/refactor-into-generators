PY_SOURCE_ROOT_DIRS = src tests

install-pip:
	python -m pip install --upgrade pip-tools pip setuptools

requirements.txt: install-pip requirements.in
	pip-compile --build-isolation --generate-hashes --output-file requirements.txt requirements.in

update-deps: requirements.txt

upgrade-deps: install-pip
	pip-compile --upgrade --build-isolation --generate-hashes --output-file requirements.txt requirements.in

init: requirements.txt
	pip install --editable .
	pip install -r requirements.txt

sync: requirements.txt
	pip-sync requirements.txt
	pip install --editable .

isort:
	isort $(PY_SOURCE_ROOT_DIRS)

black:
	black $(PY_SOURCE_ROOT_DIRS)

isort-check:
	isort --check-only $(PY_SOURCE_ROOT_DIRS)

black-check:
	black --check $(PY_SOURCE_ROOT_DIRS)

flake8:
	flake8 $(PY_SOURCE_ROOT_DIRS)

check: isort-check black-check flake8 test-all

FIB_MODULES = before before_compressed first_two_combined refactored

test-all: $(FIB_MODULES)

$(FIB_MODULES):
	pytest --fib-module=$@

fixfmt: isort black

.PHONY: all test-all $(FIB_MODULES)
