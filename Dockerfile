# Stage 1: Build the React app
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend ./
RUN npm run build

# Stage 2: Final Image with FastAPI and static frontend files
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Create a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app -s /sbin/nologin appuser

WORKDIR /app

# Copy dependency files first for layer caching
COPY backend/pyproject.toml backend/uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY backend ./

# Copy built frontend files
COPY --from=frontend-builder /app/frontend/dist /app/static

# Set permissions for the non-root user
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

# Run FastAPI, supporting Cloud Run's dynamic PORT environment variable
CMD ["sh", "-c", "uv run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
