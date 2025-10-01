.PHONY: setup app train eval lint test format

VENV?=.venv
PY?=$(VENV)/bin/python
PIP?=$(VENV)/bin/pip

setup:
	python -m venv $(VENV)
	$(PIP) install -U pip wheel
	$(PIP) install -r requirements.txt

app:
	$(VENV)/bin/streamlit run app/ui_streamlit.py

train:
	$(PY) -m src.train --config configs/train.yaml

eval:
	$(PY) -m src.eval.evaluate --config configs/train.yaml

lint:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .

format:
	$(VENV)/bin/black .

test:
	$(VENV)/bin/pytest -q
