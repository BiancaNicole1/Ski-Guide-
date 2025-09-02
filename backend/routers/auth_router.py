from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db
from models.user import User
from auth.auth import hash_password, verify_password, create_token

router = APIRouter()


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str | None = None
    city: str | None = None
    country: str | None = None
    bio: str | None = None


# /register
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    print("Received registration data:", user)
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hash_password(user.password),
        phone=user.phone,
        city=user.city,
        country=user.country,
        bio=user.bio
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created"}


# /login
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Crearea token-ului JWT
    token = create_token(user.email, f"{user.first_name} {user.last_name}")
    return {"access_token": token, "token_type": "bearer"}