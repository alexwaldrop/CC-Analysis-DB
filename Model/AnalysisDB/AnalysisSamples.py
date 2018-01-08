from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class AnalysisSamples(Base):

    __tablename__ = 'Analysis_Samples'

    analysis_id     = Column(INTEGER, ForeignKey("Analysis.analysis_id"), primary_key=True, nullable=False, index=True)
    sample_id       = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), primary_key=True, nullable=False, index=True)

    analysis        = relationship("Analysis", backref="samples")
    sample          = relationship("SharedSample", backref="analyses")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisSamples(%(id)s)>" % self.__dict__