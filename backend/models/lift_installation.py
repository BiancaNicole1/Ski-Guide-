from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LiftInstallation(Base):
    __tablename__ = "lift_installations"
    id = Column(Integer, primary_key=True, index=True)
    resort_id = Column(Integer, ForeignKey("ski_resorts.id"))
    type = Column(String)
    count = Column(Integer)
