# define the name of the virtual environment directory
VENV := venv

all: docs/index.html

docs/index.html: src/pyvibe/__init.py___ generator/generate.py
	./$(VENV)/bin/python3 generator/generate.py

# Build init.py when generate.swift changes
src/pyvibe/__init.py___: generator/generate.swift
	swift generator/generate.swift

# Rebuild the virtual environment when init.py changes
$(VENV)/bin/activate: src/pyvibe/__init.py___
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install .

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all clean
