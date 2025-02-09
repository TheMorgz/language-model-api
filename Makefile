# Variables
DOCKER_COMPOSE = docker-compose
UVICORN = uvicorn
APP_MODULE = app.main:app
HOST = 0.0.0.0
PORT = 8000

# Targets
.PHONY: help run run-docker test test-docker build-docker

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

run: ## Run the FastAPI application locally
	$(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

run-docker: ## Run the FastAPI application using Docker Compose
	$(DOCKER_COMPOSE) up

test: ## Run tests locally
	pytest tests/

test-docker: ## Run tests using Docker Compose
	$(DOCKER_COMPOSE) run tests

build-docker: ## Build the Docker images
	$(DOCKER_COMPOSE) build