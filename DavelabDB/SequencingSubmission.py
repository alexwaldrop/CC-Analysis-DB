from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, BIGINT, TINYINT


class SequencingSubmission(Base):

    __tablename__ = 'sequencing_submission'

    sub_id              = Column(INTEGER,       autoincrement=True, nullable=False)
    plex                = Column(VARCHAR(255),  default=None)
    date                = Column(DATE,          default=None)
    facility            = Column(VARCHAR(255),  default=None)
    order_id            = Column(VARCHAR(128),  default=None)
    lane_id             = Column(VARCHAR(128),  default=None)
    barcode_id          = Column(VARCHAR(128),  default=None)
    sequencing_id       = Column(VARCHAR(128),  default=None)
    sequencer           = Column(VARCHAR(128),  default=None)
    iteration           = Column(VARCHAR(128),  default=None)
    pipeline            = Column(VARCHAR(128),  default=None)
    genome              = Column(VARCHAR(128),  default=None)
    notes               = Column(LONGTEXT,      default=None)
    assay               = Column(LONGTEXT,      nullable=False)
    fastq_count         = Column(BIGINT,        default=None)
    valid               = Column(TINYINT,       default=None)

    sample_id           = Column(VARCHAR(32),   ForeignKey("shared_sample.dave_lab_id"), index=True, nullable=False)
    submission_id       = Column(INTEGER,       ForeignKey("shared_submission.id"), primary_key=True, default=None,
                                 index=True)
    demultiplex_id      = Column(INTEGER,       ForeignKey("dry_demultiplexstatistics.id"), default=None, index=True)
    library_id          = Column(INTEGER,       ForeignKey("shared_library.id"), default=None, index=True)
    organism            = Column(VARCHAR(32),   ForeignKey("shared_organism.name"), default=None, index=True)

    sharedsample        = relationship("SharedSample",              backref="seq_submission")
    sharedsubmission    = relationship("SharedSubmission",          backref="seq_submission")
    demultiplex_report  = relationship("DryDemultiplexstatistics",  backref="seq_submission")
    library             = relationship("SharedLibrary",             backref="seq_submission")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SequencingSubmission(%(id)s)>" % self.__dict__
