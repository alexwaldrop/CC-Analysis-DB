# Create one declarative Base class for model classes to extend
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from DavelabDB import *
from AnalysisDB import *

