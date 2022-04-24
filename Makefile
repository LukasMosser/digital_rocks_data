PIP := $(shell command -v pip3 2> /dev/null || command which pip 2> /dev/null)
PYTHON := $(shell command -v python3 2> /dev/null || command which python 2> /dev/null)

.PHONY: install tests doc

pipcheck:
ifndef PIP
	$(error "Ensure pip or pip3 are in your PATH")
endif
	@echo Using pip: $(PIP)

pythoncheck:
ifndef PYTHON
	$(error "Ensure python or python3 are in your PATH")
endif
	@echo Using python: $(PYTHON)

install:
	make pipcheck
	$(PIP) install -r requirements.txt && $(PIP) install .

tests:
	make pythoncheck
	pytest --verbose

doc: 
	cd docs && rm -rf source/auto_examples && rm -rf build && make html && cd ..

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf auto_examples/

lint:
	flake8 docs/ examples/ drd/ tests/