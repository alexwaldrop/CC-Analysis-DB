from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class AnalysisAssays(Base):

    __tablename__ = 'Analysis_Assays'

    analysis_id     = Column(INTEGER, ForeignKey("Analysis.analysis_id"), primary_key=True, nullable=False, index=True)
    assay_id        = Column(INTEGER, ForeignKey("assays.assay_id"), primary_key=True, nullable=False, index=True)

    analysis        = relationship("Analysis", backref="assays")
    assay           = relationship("Assays", backref="analyses")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisSamples(%(id)s)>" % self.__dict__