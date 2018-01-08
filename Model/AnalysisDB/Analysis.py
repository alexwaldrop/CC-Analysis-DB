from Model import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text, Float, Table
from sqlalchemy.orm import relationship


class Analysis(Base):
    __tablename__       = 'Analysis'

    # Analysis Columns
    analysis_id         = Column(Integer, primary_key=True, unique=True)
    name                = Column(String(45))
    description         = Column(Text)
    creation_timestamp  = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    creator_id          = Column(ForeignKey(u'auth_user.id'), nullable=False, index=True)
    analysis_type_id    = Column(ForeignKey(u'Analysis_Type.analysis_type_id'), nullable=False, index=True)
    status_id           = Column(ForeignKey(u'Analysis_Status.status_id'), nullable=False, index=True)
    error_msg           = Column(Text)
    run_time            = Column(Float)
    final_output_dir    = Column(String(150), nullable=False)
    sample_sheet        = Column(Text, nullable=False)
    run_start           = Column(DateTime)
    error_id            = Column(ForeignKey(u'Analysis_Error.error_id'), nullable=False, index=True)

    # Foreign-key relationships
    output              = relationship(u'AnalysisOutput')
    analysis_type       = relationship(u'AnalysisType')
    creator             = relationship(u'AuthUser')
    status              = relationship(u'AnalysisStatus')
    error               = relationship(u'AnalysisError')

    # Many-to-Many relationships
    reruns = relationship(
        u'Analysis',
        secondary='Analysis_Rerun',
        primaryjoin=u'Analysis.analysis_id == Analysis_Rerun.c.old_analysis_id',
        secondaryjoin=u'Analysis.analysis_id == Analysis_Rerun.c.new_analysis_id'
    )

# Join table for analysis reruns
analysis_rerun_table = Table(
    'Analysis_Rerun', Base.metadata,
    Column('old_analysis_id', ForeignKey(u'Analysis.analysis_id'), primary_key=True, nullable=False),
    Column('new_analysis_id', ForeignKey(u'Analysis.analysis_id'), primary_key=True, nullable=False, index=True)
)