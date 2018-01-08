from Model import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class AnalysisStatus(Base):

    __tablename__   = 'analysis_status'

    status_id       = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    description     = Column(VARCHAR(128),  nullable=False, unique=True)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisStatus(%(status_id)s)>" % self.__dict__