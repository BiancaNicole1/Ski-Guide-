from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from database import get_db
from models.user import User
import shutil
import os

router = APIRouter()

SECRET_KEY = "secret-jwt-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class ProfileUpdate(BaseModel):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    new_password: str | None = None
    phone: str | None = None
    city: str | None = None
    country: str | None = None
    bio: str | None = None


@router.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        user = db.query(User).filter(User.email == email).first()
        return {
            "email": user.email,
            "phone": user.phone,
            "city": user.city,
            "country": user.country,
            "bio": user.bio,
            "avatar_url": user.avatar_url
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.put("/profile")
def update_profile(data: ProfileUpdate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if not user_email:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        
        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Dacă email este trimis, îl actualizăm (opțional)
        if data.email:
            user.email = data.email
        
        if data.phone:
            user.phone = data.phone
        if data.city:
            user.city = data.city
        if data.country:
            user.country = data.country
        if data.bio:
            user.bio = data.bio
        if data.first_name:
            user.first_name = data.first_name
        if data.last_name:
            user.last_name = data.last_name

        if data.new_password:
            from auth.auth import hash_password
            user.hashed_password = hash_password(data.new_password)

        db.commit()
        return {"message": "Profil actualizat cu succes"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid")

@router.post("/update-avatar")
def update_avatar(file: UploadFile = File(...), token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token invalid")

        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        os.makedirs("avatars", exist_ok=True)
        filename = f"avatars/{email.replace('@', '_')}.jpg"

        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        user.avatar_url = filename
        db.commit()

        return {"avatar_url": filename}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token JWT invalid")
