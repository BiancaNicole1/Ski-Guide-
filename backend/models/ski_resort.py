from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class SkiResort(Base):
    __tablename__ = "ski_resorts"
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    altitude = Column(Integer, nullable=True)
    elevation_difference = Column(Integer, nullable=True)
    season = Column(String, nullable=True)
    opening_hours = Column(String, nullable=True)
    total_length_km = Column(Float, nullable=True)
    total_slopes = Column(Integer, nullable=True)

    slopes = relationship("SkiSlope", back_populates="resort")
