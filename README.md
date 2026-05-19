# CLUE BDI Portfolio Hub

A professional, modern portfolio hub showcasing projects related to cloud engineering, DevSecOps, and data intelligence. 

## Features
- **Project Grid**: Dynamic showcase of active repositories, including CLUE BDI Ingress/Gateway and PipelineGuard.
- **Unified Interface**: Integrates details, metrics, and posture findings for all connected repositories.
- **Admin Dashboard**: Secure management interface for portfolio content and metrics.
- **Contact Section**: Directly link to GitHub, LinkedIn, Email, and Resume.

## Tech Stack
- **Frontend**: React + TypeScript + Vite + Tailwind CSS + Shadcn UI
- **Backend**: FastAPI + Python + SQLAlchemy + PostgreSQL (Seeded via SQLite for local development)
- **CI/CD**: GitHub Actions (deploys to Google Cloud Run)

## Getting Started

### Local Development

1. **Install Dependencies**:
   ```bash
   make install
   ```

2. **Run Dev Environment**:
   ```bash
   make dev
   ```

3. **Backend Database Seeding**:
   The backend auto-seeds the database on startup. To seed manually:
   ```bash
   cd backend
   uv run python -m app.init_db
   ```
