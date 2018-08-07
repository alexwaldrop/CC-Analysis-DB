from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class OutputFile(Base):

    __tablename__   = 'output_file'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    task_id         = Column(VARCHAR(128),  nullable=False)

    file_id         = Column(INTEGER,       ForeignKey("file.id"), nullable=False, index=True)
    analysis_id     = Column(INTEGER,       ForeignKey("analysis.analysis_id"), nullable=False, index=True)

    analysis        = relationship("Analysis", backref="output_file")
    file            = relationship("File",     backref="output")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<OutputFile(%(id)s)>" % self.__dict__