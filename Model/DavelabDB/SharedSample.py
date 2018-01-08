from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATE, LONGTEXT, DATETIME
from sqlalchemy.ext.hybrid import hybrid_method

class SharedSample(Base):

    __tablename__ = 'shared_sample'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    dave_lab_id         = Column(VARCHAR(32),   default=None)
    old_dave_lab_id     = Column(VARCHAR(32),   default=None)
    institutional_id    = Column(VARCHAR(128),  default=None)
    preservation        = Column(VARCHAR(128),  default=None)
    material_provided   = Column(VARCHAR(128),  default=None)
    tissue              = Column(VARCHAR(128),  default=None)
    contact_person      = Column(VARCHAR(255),  default=None)
    sample_notes        = Column(LONGTEXT,      default=None)
    processing_notes    = Column(LONGTEXT,      default=None)
    experimental_notes  = Column(LONGTEXT,      default=None)
    location            = Column(LONGTEXT,      default=None)
    process_status      = Column(INTEGER,       default=None)
    date_obtained       = Column(DATE,          default=None)
    time_created        = Column(DATETIME(6),   default=None)
    time_updated        = Column(DATETIME(6),   default=None)

    patient_id          = Column(INTEGER, ForeignKey("shared_patient.dave_lab_id"), index=True, nullable=False)
    sample_type_id      = Column(VARCHAR(32), ForeignKey("shared_sampletype.name"), default=None, index=True)
    user_created_id     = Column(INTEGER, ForeignKey("auth_user.id"), default=None, index=True)
    user_updated_id     = Column(INTEGER, ForeignKey("auth_user.id"), default=None, index=True)
    project_id          = Column(VARCHAR(128), ForeignKey("shared_project.name"), default=None, index=True)

    sharedsampletype    = relationship("SharedSampletype", backref="sharedSample")
    sharedproject       = relationship("SharedProject", backref="sharedSample")
    authuser_created    = relationship("AuthUser", foreign_keys=user_created_id, backref="sharedSample_create")
    authuser_updated    = relationship("AuthUser", foreign_keys=user_updated_id, backref="sharedSample_update")
    sharedpatient       = relationship("SharedPatient", backref="sharedSample")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedSample(%(id)s)>" % self.__dict__

    @hybrid_method
    def get_submissions(self, assay_type):

        if assay_type in [1, "exome"]:
            return self.wes_submission
        elif assay_type in [2, "wg"]:
            return self.wgs_submission
        elif assay_type in [3, "rna"]:
            return self.rna_submission
        else:
            return []