from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT

class SharedLibrary(Base):

    __tablename__ = 'shared_library'

    id           = Column(INTEGER,      autoincrement=True, primary_key=True, nullable=False)
    lib_id       = Column(INTEGER,      default=None)
    source_table = Column(LONGTEXT)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedLibrary(%(id)s)>" % self.__dict__
