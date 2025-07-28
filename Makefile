.PHONY: help venv install start tests create-database

VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_FLASK = $(VENV_DIR)/bin/flask

help:
	@echo ""
	@echo " * Available commands:"
	@echo " * venv             -> Creates virtual environment (.venv)"
	@echo " * install          -> Installs dependencies from src/requirements.txt"
	@echo " * start            -> Starts the REST API (Python/Flask)"
	@echo " * tests            -> Run all tests (PyTest)"
	@echo " * create-database  -> Initializes the database"
	@echo ""

venv:
	python3 -m venv $(VENV_DIR)

install:
	$(VENV_PIP) install -r src/requirements.txt

start:
	cd src && ../$(VENV_FLASK) run

tests:
	$(VENV_PYTHON) -m pytest

create-database:
	PYTHONPATH=src $(VENV_PYTHON) -c "from app.database.init_db import init_db; init_db()"