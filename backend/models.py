from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserRegisterRequest(Base):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str = None
    city: str = None
    country: str = None
    bio: str = None

