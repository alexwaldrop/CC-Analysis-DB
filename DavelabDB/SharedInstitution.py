from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class SharedInstitution(Base):

    __tablename__ = 'shared_institution'

    id          = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name        = Column(VARCHAR(255),  nullable=False)
    location    = Column(VARCHAR(255),  default=None)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedInstitution(%(id)s)>" % self.__dict__
