# CLUE BDI Portfolio Hub Documentation

Welcome to the official developer and deployment documentation for the **CLUE BDI Portfolio Hub** project.

The CLUE BDI Portfolio Hub is a professional, modern portfolio dashboard showcasing cloud engineering, DevSecOps, and data intelligence projects. It aggregates project details, live execution statuses, and security postures for all connected CLUE BDI repositories.

## Documentation Structure

This documentation site is split into the following sections tailored for developers, operators, and administrators:

*   [**Development & Setup Guide**](dev_guide.md): Details on local setup requirements, frontend and backend installation, and database initialization.
*   [**Deployment Guide**](deploy_guide.md): Step-by-step instructions on deploying the unified portfolio app to Google Cloud Run using GitHub Actions or manual gcloud CLI commands.
*   [**API Specification**](openapi.yaml): Full OpenAPI v3 contract specifications for the portfolio backend.

---

### Core Tech Stack Summary
*   **Backend**: Python, [FastAPI](https://fastapi.tiangolo.com), SQLAlchemy, Uvicorn, Astral `uv`
*   **Frontend**: React, Vite, TypeScript, Tailwind CSS, Shadcn UI
*   **Database**: PostgreSQL (with SQLite for local development)
*   **CI/CD**: GitHub Actions (deploys to Google Cloud Run via Google Artifact Registry)
