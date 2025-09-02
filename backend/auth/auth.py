from passlib.hash import bcrypt
from jose import jwt
import datetime

SECRET_KEY = "secret-jwt-key"

def hash_password(password: str):
    return bcrypt.hash(password)

def verify_password(plain: str, hashed: str):
    return bcrypt.verify(plain, hashed)

def create_token(email: str, name: str):
    return jwt.encode(
        {
            "sub": email,
            "name": name,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )
