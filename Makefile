# define the name of the virtual environment directory
VENV := venv

all: $(VENV)/bin/activate

# Build init.py when generate.swift changes
src/pagebuilder/__init.py___: generator/generate.swift
	swift generator/generate.swift

# Rebuild the virtual environment when init.py changes
$(VENV)/bin/activate: src/pagebuilder/__init.py___
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install .

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all clean
