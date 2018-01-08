from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class AnalysisError(Base):

    __tablename__   = 'analysis_error'

    error_id        = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    description     = Column(LONGTEXT,      default=None)
    error_type      = Column(VARCHAR(128),  nullable=False, unique=True)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisError(%(id)s)>" % self.__dict__