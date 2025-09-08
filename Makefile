create-venv:
	python3 -m venv .venv
install: create-venv
	. .venv/bin/activate && python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
run: install
	. .venv/bin/activate && python3 main.py
clean:
	rm -rf .venv __pycache__ *.pyc *.pyo
.PHONY: create-venv install run clean
