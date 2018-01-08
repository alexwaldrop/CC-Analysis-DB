from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DOUBLE, BIGINT, TINYINT


class DryDemultiplexstatistic(Base):

    __tablename__ = 'dry_demultiplexstatistics'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    lane                = Column(VARCHAR(8),    default=None)
    ha_sample_id        = Column(VARCHAR(32),   default=None)
    sample_ref          = Column(VARCHAR(32),   default=None)
    barcode             = Column(VARCHAR(32),   default=None)
    description         = Column(VARCHAR(128),  default=None)
    control             = Column(VARCHAR(32),   default=None)
    project             = Column(VARCHAR(32),   default=None)
    yield_Mbase         = Column(INTEGER,       default=None)
    percent_pf_reads    = Column(DOUBLE,        default=None)
    pf_reads            = Column(BIGINT,        default=None)
    raw_reads           = Column(BIGINT,        default=None)
    percent_raw_cpl     = Column(DOUBLE,        default=None)
    perfect_index_reads = Column(BIGINT,        default=None)
    percent_pir         = Column(DOUBLE,        default=None)
    one_mismatch_reads  = Column(BIGINT,        default=None)
    percent_omr         = Column(DOUBLE,        default=None)
    percent_q30_pf      = Column(DOUBLE,        default=None)
    mean_quality_score_pf = Column(DOUBLE,      default=None)
    flowcell_id         = Column(VARCHAR(32),   default=None)
    expected            = Column(TINYINT,       nullable=False)

    sample_id           = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), default=None, index=True)
    submission_id       = Column(INTEGER, ForeignKey("shared_submission.id"), default=None, index=True)

    sharedsubmission    = relationship("SharedSubmission", backref="demux_report")
    sharedsample        = relationship("SharedSample", backref="demux_report")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<DryDemultiplexstatistic(%(id)s)>" % self.__dict__
