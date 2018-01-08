from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, DOUBLE


class DnaSheared(Base):

    __tablename__ = 'dna_sheared'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    date                = Column(DATE,          default=None)
    iteration           = Column(INTEGER,       default=None)
    input_volume        = Column(DOUBLE,        default=None)
    input_amount        = Column(DOUBLE,        default=None)
    concentration       = Column(DOUBLE,        default=None)
    size                = Column(INTEGER,       default=None)
    molarity            = Column(DOUBLE,        default=None)
    bio_analyzer_chip   = Column(VARCHAR(255),  default=None)
    notes               = Column(LONGTEXT,      default=None)
    location            = Column(VARCHAR(128),  default=None)

    sample_id           = Column(VARCHAR(32), ForeignKey("shared_sample.dave_lab_id"), index=True, nullable=False)

    sharedsample        = relationship("SharedSample", backref="dnaSheared")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<DnaSheared(%(id)s)>" % self.__dict__
