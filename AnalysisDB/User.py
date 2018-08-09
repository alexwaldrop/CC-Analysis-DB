from .. import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class User(Base):

    __tablename__ = 'user'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    first_name      = Column(VARCHAR(30),   nullable=False)
    last_name       = Column(VARCHAR(30),   nullable=False)
    email           = Column(VARCHAR(254),  nullable=False)
    davelab_user_id = Column(INTEGER,       nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<User(%(id)s)>" % self.__dict__