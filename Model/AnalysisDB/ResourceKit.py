from Model import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import relationship


class ResourceKit(Base):
    # Table for holding resource kit config files as base64 encoded strings
    __tablename__       = 'Resource_Kit'
    resource_kit_id     = Column(Integer, primary_key=True, unique=True)
    name                = Column(String(45), nullable=False)
    description         = Column(Text)
    creation_timestamp  = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    creator_id          = Column(ForeignKey(u'auth_user.id'), nullable=False, index=True)
    data                = Column(Text, nullable=False)
    creator             = relationship(u'AuthUser')