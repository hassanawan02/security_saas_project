from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Scan, Base
import random


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/history")
def get_history():
    db = SessionLocal()
    scans = db.query(Scan).all()
    db.close()

    return [
        {"email": scan.email, "breached": scan.breached}
        for scan in scans
    ]

@app.get("/breach-check")
def breach(email: str):
    db = SessionLocal()

    breached = random.choice([True, False])

    scan = Scan(email=email, breached=breached)
    db.add(scan)
    db.commit()

    db.close()

    return {
        "email": email,
        "breached": breached,
        "message": "This email was found in a data breach ⚠️" if breached
                   else "No breaches found ✅"
    }