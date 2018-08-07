from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class InputFile(Base):

    __tablename__       = 'input_file'

    id              = Column(INTEGER,   autoincrement=True, primary_key=True, nullable=False)
    analysis_id     = Column(INTEGER,   ForeignKey("analysis.analysis_id"), nullable=False, index=True)
    file_id         = Column(INTEGER,   ForeignKey("file.id"), nullable=False, index=True)

    analysis        = relationship("Analysis",  backref="input_file")
    file            = relationship("File",      backref="input")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<InputFile(%(id)s)>" % self.__dict__