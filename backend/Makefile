.PHONY: install run test lint clean

# Default target
all: install

# Install dependencies using uv
install:
	uv sync

# Run the FastAPI server using uvicorn
run:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run unit tests
test:
	PYTHONPATH=. uv run pytest tests

# Basic syntax check
lint:
	uv run python -m compileall .

# Run integration tests
test-integration:
	PYTHONPATH=. uv run pytest tests_integration

# Run all tests
test-all:
	PYTHONPATH=. uv run pytest tests tests_integration

# Clean up cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
