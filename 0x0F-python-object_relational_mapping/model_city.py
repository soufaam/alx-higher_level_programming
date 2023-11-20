#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py
 that contains the class definition of a City """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """This class create cities table in specific DB"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey(State.id), primary_key=True,
                      nullable=False)
    state = relationship(State)
