from .. import Base
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, DOUBLE, TIMESTAMP


class Analysis(Base):

    __tablename__       = 'analysis'

    analysis_id         = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name                = Column(VARCHAR(128),  default=None)
    description         = Column(LONGTEXT,      nullable=False)
    creation_timestamp  = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())
    error_msg           = Column(LONGTEXT,      default=None)
    run_time            = Column(DOUBLE,        default=None)
    cost                = Column(DOUBLE,        default=None)
    final_output_dir    = Column(LONGTEXT,      nullable=False)
    sample_sheet        = Column(LONGTEXT,      nullable=False)
    run_start           = Column(TIMESTAMP,     default=None)
    git_commit          = Column(VARCHAR(50),   default=None)


    rerun_parent_id     = Column(INTEGER, ForeignKey("analysis.analysis_id"), nullable=True, index=True)
    creator_id          = Column(INTEGER, ForeignKey("user.id"), nullable=False, index=True)
    analysis_type_id    = Column(INTEGER, ForeignKey("analysis_type.analysis_type_id"), nullable=False, index=True)
    status_id           = Column(INTEGER, ForeignKey("analysis_status.status_id"), nullable=False, index=True)
    error_id            = Column(INTEGER, ForeignKey("analysis_error.error_id"), nullable=False, index=True)

    rerun_parent        = relationship("Analysis",          backref="rerun_child", remote_side=[analysis_id])
    creator             = relationship("User",              backref="analysis")
    analysis_type       = relationship("AnalysisType",      backref="analysis")
    status              = relationship("AnalysisStatus",    backref="analysis")
    error               = relationship("AnalysisError",     backref="analysis")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Analysis(%(analysis_id)s)>" % self.__dict__