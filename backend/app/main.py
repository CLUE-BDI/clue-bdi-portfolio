from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, projects, metrics, posture, admin

app = FastAPI(title="CLUE BDI Portfolio API", version="1.0.0")

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

@app.get("/")
async def root():
    return {"message": "Welcome to CLUE BDI Portfolio API"}
