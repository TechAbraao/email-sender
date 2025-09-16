# ============================
# Makefile Settings
# By: Abraão V. S. Santos
# ============================

# ----------------------------
# Docker Settings
# ----------------------------
COMPOSE_DIR := compose
COMPOSE_FILE := src/docker/$(COMPOSE_DIR)/docker-compose.yml
ENV_FILE := src/docker/$(COMPOSE_DIR)/.env
PROJECT_NAME := email-sender

# ----------------------------
# Python Virtualenv Settings
# ----------------------------
VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_FLASK = $(VENV_DIR)/bin/flask
CELERY_PATH = src.app.celery_app.celery_app

# ----------------------------
# Colors
# ----------------------------
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m

# ============================
# Docker Compose Commands
# ============================
up:
	@echo "🚀 Starting containers..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d

down:
	@echo "🛑 Stopping and removing containers..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down

stop:
	@echo "🛑 Stopping containers (without removing)..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop

start:
	@echo "🚀 Starting stopped containers..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) start

restart: down up

logs:
	@echo "📜 Showing service logs..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) logs -f

ps:
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) ps

build:
	@echo "🏗️ Building images..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) build

clean:
	@echo "🧹 Cleaning containers, volumes, and orphan images..."
	docker compose -p $(PROJECT_NAME) --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down -v --remove-orphans
	docker system prune -f

# ============================
# Python / Local Dev Commands
# ============================
start-setup:
	python3 -m venv $(VENV_DIR) && $(VENV_PIP) install -r src/requirements.txt

start-flask:
	cd src && FLASK_APP=app.flask_app ../$(VENV_FLASK) run

start-celery:
	$(VENV_DIR)/bin/celery -A $(CELERY_PATH) worker --loglevel=info

start-flower:
	$(VENV_DIR)/bin/celery --broker=amqp://root:root@localhost:5672/ \
		-A src.app.celery_app.celery_app flower \
		--broker_api=http://root:root@localhost:15672/api/ \
		--address=127.0.0.1 \
		--port=5555

start-tests:
	$(VENV_PYTHON) -m pytest

start-tables:
	PYTHONPATH=. $(VENV_PYTHON) ./scripts/table_initializer.py

# ============================
# Help
# ============================
help:
	@echo ""
	@echo "$(RED)Available commands:$(NC)"
	@echo ""
	@echo "  Docker:"
	@echo "  $(GREEN)make up$(NC)           -> $(YELLOW)Start containers$(NC)"
	@echo "  $(GREEN)make down$(NC)         -> $(YELLOW)Stop and remove containers$(NC)"
	@echo "  $(GREEN)make stop$(NC)         -> $(YELLOW)Stop containers (keep them)$(NC)"
	@echo "  $(GREEN)make start$(NC)        -> $(YELLOW)Start stopped containers$(NC)"
	@echo "  $(GREEN)make restart$(NC)      -> $(YELLOW)Restart containers (down + up)$(NC)"
	@echo "  $(GREEN)make logs$(NC)         -> $(YELLOW)Show real-time logs$(NC)"
	@echo "  $(GREEN)make ps$(NC)           -> $(YELLOW)List active containers$(NC)"
	@echo "  $(GREEN)make build$(NC)        -> $(YELLOW)Build images$(NC)"
	@echo "  $(GREEN)make clean$(NC)        -> $(YELLOW)Remove containers, volumes, and orphan images$(NC)"
	@echo ""
	@echo "  Local Development:"
	@echo "  $(GREEN)make start-setup$(NC)  -> $(YELLOW)Create venv and install dependencies$(NC)"
	@echo "  $(GREEN)make start-flask$(NC)  -> $(YELLOW)Start Flask Application$(NC)"
	@echo "  $(GREEN)make start-celery$(NC) -> $(YELLOW)Start Celery worker$(NC)"
	@echo "  $(GREEN)make start-flower$(NC) -> $(YELLOW)Start Flower monitoring UI$(NC)"
	@echo "  $(GREEN)make start-tests$(NC)  -> $(YELLOW)Run tests (PyTest)$(NC)"
	@echo "  $(GREEN)make start-tables$(NC) -> $(YELLOW)Initialize DB tables$(NC)"
	@echo ""

.DEFAULT_GOAL := help
.PHONY: help up down stop start restart logs ps build clean start-setup start-flask start-celery start-flower start-tests start-tables
