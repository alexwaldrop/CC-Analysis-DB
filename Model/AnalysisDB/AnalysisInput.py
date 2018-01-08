from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


class AnalysisInput(Base):

    __tablename__       = 'analysis_input'

    input_id            = Column(INTEGER,   autoincrement=True, primary_key=True, nullable=False)

    analysis_id         = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=False, index=True)
    fastq_file_id       = Column(INTEGER, ForeignKey("dry_fastqfile.id"), default=None, index=True)
    analysis_output_id  = Column(INTEGER, ForeignKey("analysis_output.analysis_output_id"), default=None, index=True)

    analysis            = relationship("Analysis",          backref="input")
    fastq_file          = relationship("DryFastqfile",      backref="analyses")
    output_file         = relationship("AnalysisOutput",    backref="analyses")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisInput(%(id)s)>" % self.__dict__