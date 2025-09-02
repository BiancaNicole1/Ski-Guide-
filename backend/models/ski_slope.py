from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class SkiSlope(Base):
    __tablename__ = "ski_slopes"
    id = Column(Integer, primary_key=True, index=True)
    resort_id = Column(Integer, ForeignKey("ski_resorts.id"))
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    length = Column(Float, nullable=True)

    resort = relationship("SkiResort", back_populates="slopes")
