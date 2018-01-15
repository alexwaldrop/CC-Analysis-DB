from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT


class SequencingFastq(Base):

    __tablename__ = 'sequencing_fastq'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    verified            = Column(INTEGER,       default=None)
    current_full_path   = Column(LONGTEXT,      default=None)
    gs_path             = Column(LONGTEXT,      default=None)
    filename            = Column(VARCHAR(255),  default=None)
    ha_sample_id        = Column(VARCHAR(32),   default=None)
    barcode_id          = Column(VARCHAR(128),  default=None)
    pair_member         = Column(INTEGER,       default=None)
    flowcell_id         = Column(VARCHAR(32),   default=None)
    lane_id             = Column(VARCHAR(32),   default=None)
    barcode             = Column(VARCHAR(32),   default=None)
    date_modified       = Column(VARCHAR(255),  default=None)
    file_md5            = Column(VARCHAR(255),  default=None)
    server_fqdn         = Column(VARCHAR(128),  default=None)
    server_ip           = Column(VARCHAR(128),  default=None)

    demultiplex_id      = Column(INTEGER, ForeignKey("dry_demultiplexstatistics.id"), default=None, index=True)
    sample_id           = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), default=None, index=True)
    submission_id       = Column(INTEGER, ForeignKey("shared_submission.id"), default=None, index=True)

    demultiplex_report  = relationship("DryDemultiplexstatistics", backref="fastq_files")
    sharedsample        = relationship("SharedSample", backref="fastq_files")
    sharedsubmission    = relationship("SharedSubmission", backref="fastq_files")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<DryFastqfile(%(id)s)>" % self.__dict__
