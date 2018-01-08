from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME


class SharedUserprofile(Base):

    __tablename__ = 'shared_userprofile'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    institution     = Column(VARCHAR(100),  default=None)
    phone           = Column(VARCHAR(32),   default=None)
    address         = Column(VARCHAR(255),  default=None)
    role            = Column(VARCHAR(64),   default=None)
    last_activity   = Column(DATETIME(6),   default=None)

    group_id        = Column(INTEGER, ForeignKey("shared_usergroup.id"), default=None, index=True)
    user_id         = Column(INTEGER, ForeignKey("auth_user.id"), nullable=False)

    sharedusergroup = relationship("SharedUsergroup", backref="sharedUserprofile")
    authuser        = relationship("AuthUser", backref="sharedUserprofile")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedUserprofile(%(id)s)>" % self.__dict__
