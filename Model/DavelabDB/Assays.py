from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT


class Assays(Base):

    __tablename__ = 'assays'

    assay_id        = Column(INTEGER,       primary_key=True, nullable=False, unique=True)
    name            = Column(VARCHAR(45),   nullable=False)
    paired_end      = Column(TINYINT,       nullable=False)
    organism_id     = Column(INTEGER, ForeignKey("shared_organism.id"), nullable=False, index=True)

    organism        = relationship("SharedOrganism", backref="assays")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Assays(%(id)s)>" % self.__dict__