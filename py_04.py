# Механізм сесій в SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file:

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

