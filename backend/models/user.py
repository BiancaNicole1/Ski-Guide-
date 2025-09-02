from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
