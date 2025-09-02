from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LiftPrice(Base):
    __tablename__ = "lift_prices"
    id = Column(Integer, primary_key=True, index=True)
    resort_id = Column(Integer, ForeignKey("ski_resorts.id"))
    ride_type = Column(String)
    price_adult = Column(Float)
    price_child = Column(Float)


