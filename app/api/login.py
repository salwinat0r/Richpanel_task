# my_app/app/api/login.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import crud
from ..security.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..database import SessionLocal  # Add this import here
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/login/")
async def login(username: str, password: str):
    db = SessionLocal()
    user = crud.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
