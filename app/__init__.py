from fastapi import FastAPI
from .api import signup, login  # Update the import statement

app = FastAPI()

app.include_router(signup.router)
app.include_router(login.router)
