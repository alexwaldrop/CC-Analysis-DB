from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, DOUBLE


class RnaSeqSubmission(Base):

    __tablename__ = 'rna_seq_submission'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    date            = Column(DATE,          default=None)
    input_volume    = Column(DOUBLE,        default=None)
    input_amount    = Column(DOUBLE,        default=None)
    concentration   = Column(DOUBLE,        default=None)
    size            = Column(INTEGER,       default=None)
    molarity        = Column(DOUBLE,        default=None)
    plex            = Column(VARCHAR(255),  default=None)
    hudson_alpha    = Column(VARCHAR(255),  default=None)
    order_id        = Column(VARCHAR(128),  default=None)
    lane_id         = Column(VARCHAR(128),  default=None)
    barcode_id      = Column(VARCHAR(128),  default=None)
    rna_sequencing_id = Column(VARCHAR(128), default=None)
    sequencer       = Column(VARCHAR(128),  default=None)
    iteration       = Column(VARCHAR(128),  default=None)
    pipeline        = Column(VARCHAR(128),  default=None)
    genome          = Column(VARCHAR(128),  default=None)
    notes           = Column(LONGTEXT,      default=None)

    sample_id       = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), index=True, nullable=False)
    submission_id   = Column(INTEGER, ForeignKey("shared_submission.id"), default=None, index=True)

    sharedsubmission = relationship("SharedSubmission", backref="rna_submission")
    sharedsample    = relationship("SharedSample", backref="rna_submission")

    library_name    = synonym("rna_sequencing_id")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<RnaSeqSubmission(%(id)s)>" % self.__dict__
