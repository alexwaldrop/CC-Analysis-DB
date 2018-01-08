from Model import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME

class AuthUser(Base):

    __tablename__ = 'auth_user'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    password        = Column(VARCHAR(128),  nullable=False)
    last_login      = Column(DATETIME(6),   default=None)
    is_superuser    = Column(TINYINT,       nullable=False)
    username        = Column(VARCHAR(150),  nullable=False)
    first_name      = Column(VARCHAR(30),   nullable=False)
    last_name       = Column(VARCHAR(30),   nullable=False)
    email           = Column(VARCHAR(254),  nullable=False)
    is_staff        = Column(TINYINT,       nullable=False)
    is_active       = Column(TINYINT,       nullable=False)
    date_joined     = Column(DATETIME(6),   nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AuthUser(%(id)s)>" % self.__dict__