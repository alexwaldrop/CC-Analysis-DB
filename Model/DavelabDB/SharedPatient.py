from Model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, LONGTEXT, DATETIME


class SharedPatient(Base):

    __tablename__ = 'shared_patient'

    id                  = Column(INTEGER,       autoincrement=True, primary_key=True, nullable=False)
    dave_lab_id         = Column(INTEGER,       nullable=False)
    institutional_id    = Column(VARCHAR(255),  default=None)
    description         = Column(LONGTEXT,      default=None)
    time_created        = Column(DATETIME(6),   default=None)
    time_updated        = Column(DATETIME(6),   default=None)

    diagnosis_id        = Column(INTEGER, ForeignKey("shared_diagnosis.id"), default=None, index=True)
    group_id            = Column(VARCHAR(255), ForeignKey("shared_usergroup.name"), default=None, index=True)
    institution_id      = Column(VARCHAR(255), ForeignKey("shared_institution.name"), default=None, index=True)
    organism_id         = Column(VARCHAR(32), ForeignKey("shared_organism.name"), default=None, index=True)
    user_created_id     = Column(INTEGER, ForeignKey("auth_user.id"), default=None, index=True)
    user_updated_id     = Column(INTEGER, ForeignKey("auth_user.id"), default=None, index=True)

    shareddiagnosis     = relationship("SharedDiagnosis", backref="sharedPatient")
    authuser_created    = relationship("AuthUser", foreign_keys=user_created_id, backref="sharedPatient_create")
    authuser_updated    = relationship("AuthUser", foreign_keys=user_updated_id, backref="sharedPatient_update")
    sharedorganism      = relationship("SharedOrganism", backref="sharedPatient")
    sharedinstitution   = relationship("SharedInstitution", backref="sharedPatient")
    sharedusergroup     = relationship("SharedUsergroup", backref="sharedPatient")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SharedPatient(%(id)s)>" % self.__dict__
