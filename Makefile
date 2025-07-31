.PHONY: help start-flask start-celery start-flower start-tests start-tables start-all

VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_FLASK = $(VENV_DIR)/bin/flask
CELERY_PATH = src.app.celery_app.celery_app

RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m

help:
	@echo ""
	@echo " * $(RED)Available commands:$(NC)"
	@echo ""
	@echo " * $(GREEN)start-setup$(NC)      -> $(YELLOW)Creates virtual environment (.venv) and Installs dependencies from src/requirements.txt$(NC)"
	@echo " * $(GREEN)start-flask$(NC)      -> $(YELLOW)Starts the REST API (Python/Flask)$(NC)"
	@echo " * $(GREEN)start-celery$(NC)     -> $(YELLOW)Starts the Celery worker$(NC)"
	@echo " * $(GREEN)start-flower$(NC)     -> $(YELLOW)Starts the Flower monitoring UI$(NC)"
	@echo " * $(GREEN)start-tests$(NC)      -> $(YELLOW)Run all tests (PyTest)$(NC)"
	@echo " * $(GREEN)start-tables$(NC)     -> $(YELLOW)Initializes the tables from database$(NC)"
	@echo ""

start-setup:
	python3 -m venv $(VENV_DIR) && $(VENV_PIP) install -r src/requirements.txt

start-flask:
	cd src && FLASK_APP=app.flask_app ../$(VENV_FLASK) run

start-celery:
	$(VENV_DIR)/bin/celery -A $(CELERY_PATH) worker --loglevel=info

start-flower:
	.venv/bin/celery --broker=amqp://root:root@localhost:5672/ \
		-A src.app.celery_app.celery_app flower \
		--broker_api=http://root:root@localhost:15672/api/ \
		--address=127.0.0.1 \
		--port=5555

start-tests:
	$(VENV_PYTHON) -m pytest

start-tables:
	PYTHONPATH=src $(VENV_PYTHON) -c "from app.database.init_db import init_db; init_db()"