from .. import Base
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TEXT, TINYINT, TIMESTAMP


class SampleSheetCreator(Base):

    __tablename__           = 'sample_sheet_creator'

    sample_sheet_creator_id = Column(INTEGER,       primary_key=True, unique=True)
    name                    = Column(VARCHAR(45),   nullable=False)
    description             = Column(TEXT,          nullable=True)
    creation_timestamp      = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())
    class_name              = Column(TEXT,          nullable=False)
    min_input_size          = Column(INTEGER,       nullable=False)
    max_input_size          = Column(INTEGER,       nullable=True, default=None)
    submission_only         = Column(TINYINT,       nullable=False)

    creator_id              = Column(ForeignKey("auth_user.id"), nullable=False, index=True)

    creator                 = relationship("AuthUser")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SampleSheetCreators(%(sample_sheet_creator_id)s)>" % self.__dict__