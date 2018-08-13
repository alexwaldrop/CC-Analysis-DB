from .. import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, LONGTEXT
from sqlalchemy.ext.hybrid import hybrid_property

class SharedSubmission(Base):

    __tablename__ = 'shared_submission'

    id           = Column(INTEGER,      autoincrement=True, primary_key=True, nullable=False)
    assay        = Column(VARCHAR(32),  nullable=False)
    sub_id       = Column(INTEGER,      default=None)
    valid        = Column(TINYINT,      default=None)
    source_table = Column(LONGTEXT)

    library_id   = Column(INTEGER, ForeignKey("shared_library.id"), nullable=False, index=True)

    library      = relationship("SharedLibrary", backref="library")

    @hybrid_property
    def submission(self):
        if self.assay.name == "wg":
            return self.wgs_submission
        elif self.assay.name == "exome":
            return self.wes_submission
        elif self.assay.name == "rna":
            return self.rna_submission
        else:
            return []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedSubmission(%(id)s)>" % self.__dict__
