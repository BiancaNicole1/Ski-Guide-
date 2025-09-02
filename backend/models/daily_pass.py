from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DailyPass(Base):
    __tablename__ = "daily_passes"
    id = Column(Integer, primary_key=True, index=True)
    resort_id = Column(Integer, ForeignKey("ski_resorts.id"))
    num_days = Column(Integer)
    price_adult = Column(Float)
    price_child = Column(Float)

  