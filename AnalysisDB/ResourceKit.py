from .. import Base
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, TIMESTAMP


class ResourceKit(Base):

    __tablename__       = 'resource_kit'

    resource_kit_id     = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name                = Column(VARCHAR(128),  nullable=False)
    description         = Column(LONGTEXT)
    creation_timestamp  = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())
    data                = Column(LONGTEXT,      nullable=False)

    creator_id          = Column(ForeignKey("auth_user.id"),    nullable=False, index=True)

    creator             = relationship("AuthUser")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ResourceKit(%(resource_kit_id)s)>" % self.__dict__