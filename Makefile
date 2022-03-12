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
	isort src tests features

black:
	black src tests features

isort-check:
	isort --check-only src tests features

black-check:
	black --check src tests features

flake8:
	flake8 src tests

check: isort-check black-check flake8

fixfmt: isort black

# For building the slides
SUBDIRS = docbuild

.PHONY: all subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	[ -d $@ ] || mkdir -p $@
	$(MAKE) -C $@ -f ../Makefile.$@
