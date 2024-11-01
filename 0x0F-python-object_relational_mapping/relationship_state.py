#!/usr/bin/python3
"""create the base class and the state class that represent the table of states
in our database"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
        create the states class wich have an id and a name
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")
