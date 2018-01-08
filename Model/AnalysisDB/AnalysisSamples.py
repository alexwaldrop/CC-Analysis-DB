from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class AnalysisSamples(Base):

    __tablename__   = 'analysis_samples'

    relation_id     = Column(INTEGER,   autoincrement=True, primary_key=True, nullable=False)

    analysis_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)
    sample_id       = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"),  nullable=False, index=True)

    analysis        = relationship("Analysis",      backref="samples")
    sample          = relationship("SharedSample",  backref="analyses")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisSamples(%(relation_id)s)>" % self.__dict__