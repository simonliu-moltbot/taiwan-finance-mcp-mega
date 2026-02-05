# DevOps Makefile for Taiwan Finance MCP Mega

PYTHON = python3
PIP = pip3
VENV = .venv
APP_PATH = src/taiwan_finance_mcp_mega/server.py

.PHONY: setup run-stdio run-http clean docker-build docker-run compose-up compose-down

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

run-stdio:
	$(VENV)/bin/python $(APP_PATH) --mode stdio

run-http:
	$(VENV)/bin/python $(APP_PATH) --mode http --port 8005

compose-up:
	docker-compose up -d --build

compose-down:
	docker-compose down

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

docker-build:
	docker build -t taiwan-finance-mcp-mega .

docker-run:
	docker run -p 8005:8000 taiwan-finance-mcp-mega

test:
	$(VENV)/bin/pytest tests/test_mega_v2.py -v
