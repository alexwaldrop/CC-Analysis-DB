from Model import Base
from sqlalchemy import Column, Integer, String


class AnalysisStatus(Base):
    # Analysis status ID table
    __tablename__   = 'Analysis_Status'
    status_id       = Column(Integer, primary_key=True, unique=True)
    description     = Column(String(45), nullable=False, unique=True)