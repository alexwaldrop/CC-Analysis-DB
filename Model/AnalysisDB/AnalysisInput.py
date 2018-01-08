from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class AnalysisInput(Base):

    __tablename__ = 'Analysis_Input'

    input_id        = Column(INTEGER, primary_key=True, autoincrement=True)
    analysis_id     = Column(INTEGER, ForeignKey("Analysis.analysis_id"), nullable=False, index=True)
    fastq_file_id   = Column(INTEGER, ForeignKey("dry_fastqfile.id"), nullable=True,
                             unique=False, index=True, default=None)
    analysis_output_id = Column(INTEGER, ForeignKey("Analysis_Output.analysis_output_id"),
                                unique=False, nullable=True, index=True, default=None)

    analysis        = relationship("Analysis", backref="input")
    fastq_file      = relationship("DryFastqfile", backref="analyses")
    output_file     = relationship("AnalysisOutput", backref="analyses")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisInput(%(id)s)>" % self.__dict__