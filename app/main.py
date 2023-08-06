# my_app/app/main.py
from fastapi import FastAPI
from .api import signup, login

app = FastAPI()

# Include API Routers
app.include_router(signup.router)
app.include_router(login.router)
