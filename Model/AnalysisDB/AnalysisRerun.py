from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class AnalysisRerun(Base):

    __tablename__       = 'analysis_rerun'

    rerun_id            = Column(INTEGER,   autoincrement=True, primary_key=True, nullable=False)

    old_analysis_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)
    new_analysis_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)

    old_analysis        = relationship("Analysis", foreign_keys=old_analysis_id, backref="rerun")
    new_analysis        = relationship("Analysis", foreign_keys=new_analysis_id)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisRerun(%(rerun_id)s)>" % self.__dict__