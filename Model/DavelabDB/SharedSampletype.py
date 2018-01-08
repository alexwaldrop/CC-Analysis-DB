from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class SharedSampletype(Base):

    __tablename__ = 'shared_sampletype'

    id          = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name        = Column(VARCHAR(32),   nullable=False)
    description = Column(LONGTEXT,      default=None)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedSampletype(%(id)s)>" % self.__dict__
