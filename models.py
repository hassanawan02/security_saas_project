from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    breached = Column(Boolean)