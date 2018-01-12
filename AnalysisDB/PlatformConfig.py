from .. import Base
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, TIMESTAMP


class PlatformConfig(Base):

    __tablename__       = 'platform_config'

    platform_config_id  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name                = Column(VARCHAR(128),  nullable=False)
    description         = Column(LONGTEXT)
    creation_timestamp  = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())
    data                = Column(LONGTEXT,      nullable=False)

    creator_id          = Column(ForeignKey("auth_user.id"),    nullable=False, index=True)

    creator             = relationship("AuthUser")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<PlatformConfig(%(platform_config_id)s)>" % self.__dict__