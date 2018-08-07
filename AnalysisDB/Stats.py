from .. import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT

class Stats(Base):

    __tablename__ = 'stats'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    sample_id       = Column(INTEGER,       nullable=False)
    key             = Column(VARCHAR(128),  nullable=False)
    value           = Column(LONGTEXT,      nullable=False)
    input_file      = Column(LONGTEXT,      nullable=False)
    task_id         = Column(LONGTEXT,      nullable=False)
    notes           = Column(LONGTEXT,      nullable=False)

    analysis_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)

    analysis        = relationship("Analysis", backref="stats")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Stats(%(id)s)>" % self.__dict__