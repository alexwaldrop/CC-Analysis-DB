from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, TINYINT


class Pipeline(Base):

    __tablename__       = 'pipeline'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name                = Column(VARCHAR(128),  nullable=False)
    description         = Column(LONGTEXT,      default=None)
    is_upstream         = Column(TINYINT,       default=None)

    analysis_type_id    = Column(INTEGER, ForeignKey("analysis_type.analysis_type_id"), nullable=False)
    creator_id          = Column(INTEGER, ForeignKey("user.id"), nullable=False, index=True)

    analysis_type       = relationship("AnalysisType",  backref="pipeline")
    creator             = relationship("User")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Pipeline(%(id)s)>" % self.__dict__