from .. import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

class WhoSubmissionAnalysis(Base):

    __tablename__ = 'who_submission_analysis'

    id              = Column(INTEGER,   autoincrement=True, primary_key=True, nullable=False)
    analysis_id     = Column(INTEGER,   nullable=False)

    submission_id   = Column(INTEGER,   ForeignKey("who_submission_analysis.id"), nullable=False, index=True)

    submission      = relationship("WhoSubmission", backref="analysis")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<WhoSubmissionAnalysis(%(id)s)>" % self.__dict__