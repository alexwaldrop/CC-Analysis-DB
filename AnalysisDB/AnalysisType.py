from .. import Base
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
    max_run_time            = Column(DOUBLE,        nullable=False, default=72)
    paired_end              = Column(TINYINT,       nullable=False, default=1)
    graph_config            = Column(LONGTEXT,      nullable=False)
    platform_config         = Column(LONGTEXT,      nullable=False)
    resource_kit            = Column(LONGTEXT,      nullable=False)
    ssc_class_name          = Column(VARCHAR(128),  nullable=False)

    creator_id              = Column(INTEGER, ForeignKey("user.id"), nullable=False, index=True)

    creator                 = relationship("User",    backref="analysis_types")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<AnalysisType(%(analysis_type_id)s)>" % self.__dict__