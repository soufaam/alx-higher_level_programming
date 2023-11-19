#!/usr/bin/python3
"""A Write a python file that contains the class definition
of a State and an instance Base = declarative_base():"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class create states table in specific DB"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
