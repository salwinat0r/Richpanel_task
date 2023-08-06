# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from .api import login, signup

app = FastAPI()

# Serve index.html from the frontend/static/ directory
@app.get("/", response_class=FileResponse)
async def read_index():
    return "frontend/static/index.html"

# Serve static files from the frontend/static/ directory
app.mount("/static", StaticFiles(directory="frontend/static/", html=True), name="static")

# Include API Routers
app.include_router(login.router)
app.include_router(signup.router)
