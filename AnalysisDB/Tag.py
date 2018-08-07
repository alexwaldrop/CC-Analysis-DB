from .. import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT

class Tag(Base):

    __tablename__ = 'tag'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    tag             = Column(LONGTEXT,      nullable=False)

    analysis_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)

    analysis        = relationship("Analysis", backref="tag")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Tag(%(id)s)>" % self.__dict__