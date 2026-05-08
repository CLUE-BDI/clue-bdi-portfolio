.PHONY: dev backend frontend install

# Default target
all: dev

# Run both frontend and backend using concurrently
dev:
	npm run dev

# Run only backend
backend:
	cd backend && make run

# Run only frontend
frontend:
	cd frontend && npm run dev

# Install all dependencies
install:
	npm install
	cd backend && uv sync
