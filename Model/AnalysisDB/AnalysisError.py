from Model import Base
from sqlalchemy import Column, Integer, Text, String


class AnalysisError(Base):
    # Analysis error ID table
    __tablename__   = 'Analysis_Error'
    error_id        = Column(Integer, primary_key=True, unique=True)
    description     = Column(Text)
    error_type      = Column(String(45), nullable=False, unique=True)