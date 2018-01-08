from Model import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text, Float
from sqlalchemy.orm import relationship


class AnalysisType(Base):
    # Table for holding all data needed to run an analysis
    __tablename__           = 'Analysis_Type'

    analysis_type_id        = Column(Integer, primary_key=True, nullable=False, unique=True)
    name                    = Column(String(45), nullable=False)
    description             = Column(Text)
    creator_id              = Column(ForeignKey(u'auth_user.id'), nullable=False, index=True)
    creation_timestamp      = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    graph_config_id         = Column(ForeignKey(u'Graph_Config.graph_config_id'), nullable=False, index=True)
    resource_kit_id         = Column(ForeignKey(u'Resource_Kit.resource_kit_id'), primary_key=True, nullable=False, index=True)
    platform_config_id      = Column(ForeignKey(u'Platform_Config.platform_config_id'), nullable=False, index=True)
    startup_script_id       = Column(ForeignKey(u'Startup_Script.startup_script_id'), index=True)
    sample_sheet_creator_id = Column(ForeignKey("Sample_Sheet_Creators.sample_sheet_creator_id"), nullable=False, index=True)
    cpus                    = Column(Integer, nullable=False)
    mem                     = Column(Integer, nullable=False)
    disk_space              = Column(Integer, nullable=False)
    max_run_time            = Column(Float, nullable=False, server_default=text("24.0"))

    creator                 = relationship(u'AuthUser')
    graph_config            = relationship(u'GraphConfig')
    platform_config         = relationship(u'PlatformConfig')
    resource_kit            = relationship(u'ResourceKit')
    startup_script          = relationship(u'StartupScript')
    sample_sheet_creator    = relationship("SampleSheetCreators")