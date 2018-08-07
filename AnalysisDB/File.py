from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class File(Base):

    __tablename__       = 'file'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    file_type           = Column(VARCHAR(32),   nullable=False)
    path                = Column(LONGTEXT,      nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<File(%(id)s)>" % self.__dict__