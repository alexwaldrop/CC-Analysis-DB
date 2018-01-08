from Model import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TEXT, TINYINT


class SampleSheetCreators(Base):

    __tablename__ = 'Sample_Sheet_Creators'

    sample_sheet_creator_id = Column(INTEGER,       primary_key=True, unique=True)
    name                    = Column(VARCHAR(45),   nullable=False)
    description             = Column(TEXT,          nullable=True)
    class_name              = Column(TEXT,          nullable=False)
    min_input_size          = Column(INTEGER,       nullable=False)
    max_input_size          = Column(INTEGER,       nullable=True, default=None)
    submission_only         = Column(TINYINT,       nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<SampleSheetCreators(%(id)s)>" % self.__dict__