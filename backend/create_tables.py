from database import Base, engine
import models  # atenție: aici trebuie să fie importat models ca să încarce toate clasele

# aici efectiv creează toate tabelele
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
