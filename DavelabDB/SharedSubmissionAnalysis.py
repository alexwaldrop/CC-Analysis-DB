from .. import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

class SharedSubmissionAnalysis(Base):

    __tablename__ = 'shared_submissionanalysis'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    analysis_id     = Column(INTEGER,       nullable=False)
    pipeline        = Column(VARCHAR(128),  nullable=False)

    submission_id   = Column(INTEGER,   ForeignKey("shared_submission.id"), nullable=False, index=True)
    user_id         = Column(INTEGER,   ForeignKey("auth_user.id"), nullable=False)

    submission      = relationship("SharedSubmission",  backref="analysis")
    user            = relationship("AuthUser",          backref="analysis")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<WhoSubmissionAnalysis(%(id)s)>" % self.__dict__