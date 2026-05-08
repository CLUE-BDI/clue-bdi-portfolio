.PHONY: install run test lint clean

# Default target
all: install

# Install dependencies using uv
install:
	uv sync

# Run the FastAPI server using uvicorn
run:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run tests using pytest
test:
	uv run pytest

# Basic syntax check
lint:
	uv run python -m compileall .

# Clean up cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
