# Deployment Guide - CLUE BDI Portfolio Hub

This guide details the deployment process for the CLUE BDI Portfolio Hub to Google Cloud Run.

## Continuous Integration & Deployment (CI/CD)

The application uses GitHub Actions to automate testing and deployment. The workflow is defined in `.github/workflows/ci-cd.yml`.

### Workflow Stages
1. **Frontend Tests**: Uses Node.js 20 to install dependencies and run Vitest/Jest unit tests.
2. **Backend Unit Tests**: Uses Astral `uv` tool to set up Python 3.12, sync dependencies, and run unit tests.
3. **Backend Integration Tests**: Runs database-backed API integration tests.
4. **Deploy**: Builds the Docker image, pushes it to Google Artifact Registry, and deploys it to Google Cloud Run.

### GitHub Actions Secrets
The following secrets must be configured in the GitHub repository Settings -> Secrets and variables -> Actions:
- `GCP_PROJECT_ID`: The ID of your Google Cloud Project.
- `GCP_CREDENTIALS`: A JSON Service Account key with Cloud Run Admin, Artifact Registry Writer, and Storage Admin permissions.

## Manual Deployment

To deploy manually using the Google Cloud SDK:

1. **Build and push the Docker image**:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/clue-bdi-portfolio
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy clue-bdi-portfolio \
     --image gcr.io/YOUR_PROJECT_ID/clue-bdi-portfolio \
     --platform managed \
     --region us-east1 \
     --allow-unauthenticated
   ```
