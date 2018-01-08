from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class SharedUsergroup(Base):

    __tablename__ = 'shared_usergroup'

    id          = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name        = Column(VARCHAR(255),  nullable=False)
    description = Column(LONGTEXT,      default=None)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedUsergroup(%(id)s)>" % self.__dict__
