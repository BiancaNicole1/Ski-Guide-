import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SkiResort, SkiSlope, DailyPass, LiftInstallation

# deschide fișierul JSON
with open('ski_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# pornim sesiunea SQLAlchemy
db: Session = SessionLocal()

for resort_data in data:
    # adăugăm resortul principal
    resort = SkiResort(
        slug=resort_data['id'],
        name=resort_data['name'],
        location=resort_data['location'],
        altitude=resort_data['altitude'],
        total_slopes=resort_data['numberOfSlopes'],
        season=resort_data['season']
    )
    db.add(resort)
    db.commit()
    db.refresh(resort)  # important: acum avem resort.id generat

    # adăugăm pârtiile asociate
    for slope_data in resort_data['slopes']:
        slope = SkiSlope(
            resort_id=resort.id,
            name=slope_data['name'],
            difficulty=slope_data['difficulty'],
            length=slope_data['lengthKm']
        )
        db.add(slope)

    # adăugăm prețurile zilnice simplificate (day / week)
    for price_data in resort_data['prices']:
        daily_pass = DailyPass(
            resort_id=resort.id,
            num_days=1 if price_data['week'] == 0 else 7,  # adaptăm după caz
            price_adult=price_data['day'] if price_data['type'] == 'adult' else 0,
            price_child=price_data['day'] if price_data['type'] == 'child' else 0
        )
        db.add(daily_pass)

    # adăugăm facilitățile (le mapăm doar pe cele de tip instalație)
    for facility_data in resort_data['facilities']:
        if facility_data['type'] in ['telecabină', 'telegondolă', 'telescaun', 'teleski']:
            lift = LiftInstallation(
                resort_id=resort.id,
                type=facility_data['type'],
                count=1  # momentan presupunem 1 (pentru că JSON-ul tău nu are count real)
            )
            db.add(lift)

    db.commit()

db.close()
