# CLUE BDI Portfolio Hub Developer Setup Guide

This guide describes how to configure, set up, and run the **CLUE BDI Portfolio Hub** application locally.

---

## 🛠️ 1. Prerequisites & Environment Setup

Ensure you have the following prerequisites installed on your local system:
- **Python**: Version 3.12 or higher.
- **Node.js**: Version 20 or higher.
- **Astral `uv`**: Python package and dependency manager.

---

## 🚀 2. Getting Started (Installation)

We provide a `Makefile` to quickly bootstrap both the frontend and backend dependencies.

### Step 2.1: Install Dependencies
Run the installation target to initialize the python virtual environment and node modules:
```bash
make install
```
This command runs:
*   `uv sync` in the backend directory.
*   `npm install` in the frontend directory.

### Step 2.2: Run Development Servers
Run the development environment to start both frontend and backend servers concurrently:
```bash
make dev
```
Once running, you can access the applications at:
*   **Frontend**: `http://localhost:5173/`
*   **Backend API**: `http://localhost:8000/`

---

## 🗄️ 3. Database Initialization & Seeding

For local development, the backend automatically initializes and seeds a local SQLite database on startup.

If you need to manually drop and re-seed the database records:
```bash
cd backend
uv run python -m app.init_db
```
This runs the seeding scripts which populate:
*   Connected repositories (`global-tracker-spark`, `blue-green-gateway`, `pipelineguard`, etc.)
*   Project metadata, links (e.g. Resume URL, Git links), and status flags.
