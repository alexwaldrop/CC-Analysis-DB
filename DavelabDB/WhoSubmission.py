from .. import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, TIMESTAMP

class WhoSubmission(Base):

    __tablename__ = 'who_submission'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    sequencing_id   = Column(VARCHAR(32),   default=None)
    library_id      = Column(VARCHAR(32),   default=None)
    received        = Column(TINYINT(1),    nullable=False, default=0)
    valid           = Column(TINYINT(1),    nullable=False, default=0)
    time            = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())

    sample_id       = Column(VARCHAR(32),   ForeignKey("shared_sample.dave_lab_id"), nullable=False, index=True)

    sample          = relationship("SharedSample", backref="who_submission")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<WhoSubmission(%(id)s)>" % self.__dict__