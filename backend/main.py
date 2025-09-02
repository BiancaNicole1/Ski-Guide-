from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import auth_router, profile_router, recommendation_router,resorts_router, ai_recommend
from models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS – permite conectarea de pe mobil / frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creează tabelele în DB
Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
app.include_router(profile_router.router)
app.include_router(recommendation_router.router)
app.include_router(resorts_router.router)
app.include_router(ai_recommend.router)

#optional - pt testare 
@app.get("/")
def read_root():
    return {"message": "Backend is running"}


