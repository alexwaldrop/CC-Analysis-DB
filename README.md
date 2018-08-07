# DatabaseModel

SqlAlchemy ORM for Lab database and Analysis database.

## Create a new database

To create a database from scratch using the defined SqlAlchemy ORM, please run the following script:

```python
from DatabaseModel import Base
from sqlalchemy import create_engine

# Create Engine
#   Example:
#       engine = create_engine("mysql://gap:XXXXXXXXXX@104.196.X.X/AnalysisDB")
engine = create_engine("*driver*://*username*:*password*@*host_ip*[:*port*]/*Database*")

# Create all tables
Base.metadata.create_all(bind=engine)
```