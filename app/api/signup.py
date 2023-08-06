# my_app/app/api/signup.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import crud
from ..database.schemas import UserCreate
from ..security.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from ..database import SessionLocal  # Add this import here

router = APIRouter()

@router.post("/signup/")
async def signup(user: UserCreate):
    db = SessionLocal()
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already taken")

    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user = crud.create_user(db, user)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
