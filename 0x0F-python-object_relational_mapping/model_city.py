#!/usr/bin/python3
"""create the base class and the city class that represent the table of cities
in our database"""


from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
        create the cities class wich have an id and a name
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True)
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
