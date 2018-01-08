from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, DOUBLE


class RnaCapturedLibrary(Base):

    __tablename__ = 'rna_captured_library'

    id              = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    iteration       = Column(INTEGER,       default=None)
    date            = Column(DATE,          default=None)
    input_volume    = Column(DOUBLE,        default=None)
    input_amount    = Column(DOUBLE,        default=None)
    method          = Column(VARCHAR(128),  default=None)
    volume_baits    = Column(INTEGER,       default=None)
    pcr_cycles      = Column(INTEGER,       default=None)
    tube            = Column(VARCHAR(128),  default=None)
    size            = Column(INTEGER,       default=None)
    concentration   = Column(DOUBLE,        default=None)
    molarity        = Column(DOUBLE,        default=None)
    notes           = Column(LONGTEXT,      default=None)
    location        = Column(VARCHAR(128),  default=None)

    sample_id       = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), index=True, nullable=False)

    sharedsample    = relationship("SharedSample", backref="rnaCapturedLibrary")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<RnaCapturedLibrary(%(id)s)>" % self.__dict__
