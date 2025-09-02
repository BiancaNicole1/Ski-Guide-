from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, conint, constr
from typing import Literal

router = APIRouter()

class EquipmentRequest(BaseModel):
    height: conint(gt=80, lt=250)  # înălțime 80–250 cm
    weight: conint(gt=20, lt=250)  # greutate 20–250 kg
    level: Literal["beginner", "novice", "intermediate", "advanced"]

class EquipmentResponse(BaseModel):
    recommended_ski_length: int
    recommended_boot_size: str
    explanation: dict

@router.post("/recommend-equipment", response_model=EquipmentResponse)
def recommend_equipment(data: EquipmentRequest):
    """
    Returnează lungimea recomandată a schiurilor și mărimea clăparilor (Mondopoint)
    pe baza înălțimii, greutății și nivelului de experiență.
    """

    # 1. Procent de bază în funcție de nivel
    level_percent = {
        "beginner": 0.88,
        "novice": 0.90,
        "intermediate": 0.93,
        "advanced": 0.98,
    }
    percent = level_percent[data.level]

    # Calcul lungime schi
    ski_length = int(data.height * percent)
    if data.weight < 60:
        ski_length -= 5
    elif data.weight > 90:
        ski_length += 5

    # 2. Mărimea clăparilor – sistem Mondopoint
    # Mondopoint = lungimea piciorului în mm (ISO standard) :contentReference[oaicite:6]{index=6}
    # Estimăm lungimea piciorului ca 15% din înălțime (valoare aprox. utilă)
    foot_length_cm = data.height * 0.15
    mondopoint_mm = round(foot_length_cm * 10)  # transformăm în mm

    boot_size = f"{mondopoint_mm} mm (Mondopoint)"

    # 3. Explicații detaliate
    explanation = {
        "ski": (
            f"Lungimea schiurilor este calculată ca {percent*100:.0f}% din înălțimea ta "
            f"({data.height} cm), ajustată cu greutatea ({data.weight} kg): {ski_length} cm."
        ),
        "boots": (
            f"Aproximăm lungimea piciorului ca 15% din înălțime → {foot_length_cm:.1f} cm "
            f"=> {mondopoint_mm} mm în sistem Mondopoint (lungime standard măsurată între călcâi și vârful degetului, ISO)."  
        )
    }

    return {
        "recommended_ski_length": ski_length,
        "recommended_boot_size": boot_size,
        "explanation": explanation
    }
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, conint, constr
from typing import Literal

router = APIRouter()

class EquipmentRequest(BaseModel):
    height: conint(gt=80, lt=250)  # înălțime 80–250 cm
    weight: conint(gt=20, lt=250)  # greutate 20–250 kg
    level: Literal["beginner", "novice", "intermediate", "advanced"]

class EquipmentResponse(BaseModel):
    recommended_ski_length: int
    recommended_boot_size: str
    explanation: dict

@router.post("/recommend-equipment", response_model=EquipmentResponse)
def recommend_equipment(data: EquipmentRequest):
    """
    Returnează lungimea recomandată a schiurilor și mărimea clăparilor (Mondopoint)
    pe baza înălțimii, greutății și nivelului de experiență.
    """

    # 1. Procent de bază în funcție de nivel
    level_percent = {
        "beginner": 0.88,
        "novice": 0.90,
        "intermediate": 0.93,
        "advanced": 0.98,
    }
    percent = level_percent[data.level]

    # Calcul lungime schi
    ski_length = int(data.height * percent)
    if data.weight < 60:
        ski_length -= 5
    elif data.weight > 90:
        ski_length += 5

    # 2. Mărimea clăparilor – sistem Mondopoint
    # Mondopoint = lungimea piciorului în mm (ISO standard) :contentReference[oaicite:6]{index=6}
    # Estimăm lungimea piciorului ca 15% din înălțime (valoare aprox. utilă)
    foot_length_cm = data.height * 0.15
    mondopoint_mm = round(foot_length_cm * 10)  # transformăm în mm

    boot_size = f"{mondopoint_mm} mm (Mondopoint)"

    # 3. Explicații detaliate
    explanation = {
        "ski": (
            f"Lungimea schiurilor este calculată ca {percent*100:.0f}% din înălțimea ta "
            f"({data.height} cm), ajustată cu greutatea ({data.weight} kg): {ski_length} cm."
        ),
        "boots": (
            f"Aproximăm lungimea piciorului ca 15% din înălțime → {foot_length_cm:.1f} cm "
            f"=> {mondopoint_mm} mm în sistem Mondopoint (lungime standard măsurată între călcâi și vârful degetului, ISO)."  
        )
    }

    return {
        "recommended_ski_length": ski_length,
        "recommended_boot_size": boot_size,
        "explanation": explanation
    }
