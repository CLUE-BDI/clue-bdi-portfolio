.PHONY: dev backend frontend install up down logs ps

# Default target
all: dev

# ── Docker Compose (production-like) ──────────────────────────────────────────

# Build and start all containers (Postgres + FastAPI + Nginx/React)
up:
	docker compose up --build

# Start in detached mode
up-d:
	docker compose up --build -d

# Stop and remove containers (keeps the postgres_data volume)
down:
	docker compose down

# Stop and remove containers AND wipe the database volume
down-v:
	docker compose down -v

# Tail logs from all services
logs:
	docker compose logs -f

# Show running container status
ps:
	docker compose ps

# ── Local Development (no Docker) ─────────────────────────────────────────────

# Run both frontend and backend using concurrently
dev:
	npm run dev

# Run only backend
backend:
	cd backend && make run

# Run only frontend
frontend:
	cd frontend && npm run dev

# Run integration tests
test-integration:
	cd backend && PYTHONPATH=. uv run pytest tests_integration

# Run all tests (unit + integration)
test:
	cd backend && PYTHONPATH=. uv run pytest tests tests_integration

# Install all dependencies
install:
	npm install
	cd backend && uv sync
