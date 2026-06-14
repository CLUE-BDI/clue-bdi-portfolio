from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routers import auth, projects, metrics, posture, admin, demo_requests
from .init_db import init_db
import os
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize and seed database
    init_db()
    yield
    # Shutdown logic (if any) goes here

app = FastAPI(title="CLUE BDI Portfolio API", version="1.0.0", lifespan=lifespan)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(projects.router, prefix="/api/v1")
app.include_router(metrics.router, prefix="/api/v1")
app.include_router(posture.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")
app.include_router(demo_requests.router, prefix="/api/v1")

# Serve frontend static files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if os.path.isdir(static_dir):
    # Mount assets so they are served directly
    assets_dir = os.path.join(static_dir, "assets")
    if os.path.isdir(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.api_route("/{full_path:path}", methods=["GET", "HEAD"])
    async def serve_spa(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not Found"}, status_code=404)
        
        file_path = os.path.join(static_dir, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        
        index_path = os.path.join(static_dir, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
        
        return JSONResponse({"detail": "Not Found"}, status_code=404)
else:
    @app.get("/")
    async def root():
        return {"message": "Welcome to CLUE BDI Portfolio API"}
