from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, DOUBLE


class DnaExtraction(Base):

    __tablename__ = 'dna_extraction'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    date                = Column(DATE,          default=None)
    iteration           = Column(INTEGER,       default=None)
    method              = Column(VARCHAR(128),  default=None)
    elution_solution    = Column(VARCHAR(128),  default=None)
    volume_eluted       = Column(INTEGER,       default=None)
    concentration       = Column(DOUBLE,        default=None)
    notes               = Column(LONGTEXT,      default=None)
    location            = Column(VARCHAR(128),  default=None)

    sample_id           = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), index=True, nullable=False)

    sharedsample        = relationship("SharedSample", backref="dnaExtraction")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<DnaExtraction(%(id)s)>" % self.__dict__
