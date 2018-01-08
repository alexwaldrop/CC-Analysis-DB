from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class AnalysisOutput(Base):

    __tablename__       = 'analysis_output'

    analysis_output_id  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    node_id             = Column(VARCHAR(128),  nullable=False)
    output_key          = Column(VARCHAR(128),  nullable=False)
    path                = Column(LONGTEXT,      nullable=False)

    analysis_id         = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)

    analysis            = relationship("Analysis", backref="output")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisOutput(%(id)s)>" % self.__dict__