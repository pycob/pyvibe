# define the name of the virtual environment directory
VENV := venv

all: venv docs/index.html

venv: $(VENV)/bin/activate

flask:
	./$(VENV)/bin/pip install flask
	./$(VENV)/bin/python3 integration_tests/flask_test.py

docs/index.html: src/pyvibe/__init.py___ generator/generate.py
	./$(VENV)/bin/pip install pandas
	./$(VENV)/bin/python3 generator/generate.py

# pdoc: src/pyvibe/__init.py___
# 	./$(VENV)/bin/pip install pdoc
# 	./$(VENV)/bin/pdoc pyvibe --logo https://cdn.pycob.com/pycob_hex.png --logo-link https://www.pyvibe.com --no-show-source -e pycob=https://github.com/pycob/pyvibe/tree/main/src/pyvibe/ -n --docformat google -o docs/pdoc/

# Build init.py when generate.swift changes
src/pyvibe/__init.py___: generator/generate.swift
	swift generator/generate.swift

# Rebuild the virtual environment when init.py changes
$(VENV)/bin/activate: src/pyvibe/__init.py___
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install .

screenshot:
	./$(VENV)/bin/pip install selenium
	sudo ./$(VENV)/bin/python3 generator/screenshot.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all clean flask screenshot
