from Model import Base
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, DOUBLE, TIMESTAMP, TINYINT


class AnalysisType(Base):

    __tablename__           = 'analysis_type'

    analysis_type_id        = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    name                    = Column(VARCHAR(128),  nullable=False)
    description             = Column(LONGTEXT,      default=None)
    creation_timestamp      = Column(TIMESTAMP,     nullable=False, server_default=func.current_timestamp())
    cpus                    = Column(INTEGER,       nullable=False)
    mem                     = Column(INTEGER,       nullable=False)
    disk_space              = Column(INTEGER,       nullable=False)
    max_run_time            = Column(DOUBLE,        nullable=False, default=24)
    paired_end              = Column(TINYINT,       nullable=False, default=1)
    assay                   = Column(VARCHAR(5))

    creator_id              = Column(INTEGER, ForeignKey("auth_user.id"), nullable=False, index=True)
    graph_config_id         = Column(INTEGER, ForeignKey("graph_config.graph_config_id"), nullable=False, index=True)
    resource_kit_id         = Column(INTEGER, ForeignKey("resource_kit.resource_kit_id"), nullable=False, index=True)
    platform_config_id      = Column(INTEGER, ForeignKey("platform_config.platform_config_id"), nullable=False, index=True)
    startup_script_id       = Column(INTEGER, ForeignKey("startup_script.startup_script_id"), nullable=False, index=True)
    sample_sheet_creator_id = Column(INTEGER, ForeignKey("sample_sheet_creator.sample_sheet_creator_id"), nullable=False, index=True)

    creator                 = relationship("AuthUser",              backref="analysis_types")
    graph_config            = relationship("GraphConfig",           backref="analysis_types")
    platform_config         = relationship("PlatformConfig",        backref="analysis_types")
    resource_kit            = relationship("ResourceKit",           backref="analysis_types")
    startup_script          = relationship("StartupScript",         backref="analysis_types")
    sample_sheet_creator    = relationship("SampleSheetCreator",    backref="analysis_types")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisType(%(analysis_type_id)s)>" % self.__dict__