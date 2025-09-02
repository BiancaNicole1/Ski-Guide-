from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List, Optional, Union
import google.generativeai as genai

genai.configure(api_key="AIzaSyA_cgvKvshXbDpH8uE12DO5F88beE80wBE")

router = APIRouter()

class ResortPreferences(BaseModel):
    difficulty: str
    region: str
    preferences: List[str]
    additional_notes: str = ""

class QueryMessage(BaseModel):
    query: str

@router.post("/ai-ski-recommendation")
def ai_recommendation(data: Union[ResortPreferences, QueryMessage]):
    if isinstance(data, QueryMessage):
        prompt = data.query
    else:
        prompt = f"""
Sunt un utilizator care preferă pârtii de dificultate {data.difficulty}, în zona {data.region}.
Preferințele mele includ: {", ".join(data.preferences)}.
{f"Note adiționale: {data.additional_notes}" if data.additional_notes else ""}

Recomandă-mi o stațiune din România care se potrivește profilului meu, explicând de ce.
"""
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return { "recomandare": response.text.strip() }
