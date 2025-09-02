from pydantic import BaseModel
from typing import List, Optional

class SlopeSchema(BaseModel):
    name: str
    difficulty: str
    length_km: float
    is_open: bool
    color: Optional[str] = None
    icon: Optional[str] = None

class FacilitySchema(BaseModel):
    type: str
    description: str

class PriceSchema(BaseModel):
    type: str
    day: int
    week: int

class LiftPriceSchema(BaseModel):
    category: str
    label: str
    adult_price: str
    child_price: str
    extra_info: Optional[str] = None

class FaqSchema(BaseModel):
    question: str
    answer: str

class ResortDetailSchema(BaseModel):
    id: int
    slug: str
    name: str
    location: str
    altitude: int
    elevation_difference: int
    season: str
    opening_hours: str
    total_length_km: float
    total_slopes: int
    slopes: List[SlopeSchema]
    facilities: List[FacilitySchema]
    prices: List[PriceSchema]
    liftPrices: dict
    faqs: List[FaqSchema]
