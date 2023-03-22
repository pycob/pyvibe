# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv run

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 main.py

deploy: venv
	./$(VENV)/bin/python3 -m pycob.deploy

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean deploy