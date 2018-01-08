from Model import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text


class AnalysisOutput(Base):
    # Table for holding output files associated with an analysis
    __tablename__       = 'Analysis_Output'
    analysis_output_id  = Column(Integer, primary_key=True, unique=True)
    node_id             = Column(String(45), nullable=False)
    output_key          = Column(String(45), nullable=False)
    path                = Column(Text)
    analysis_id         = Column(ForeignKey(u'Analysis.analysis_id'), nullable=False, index=True)
