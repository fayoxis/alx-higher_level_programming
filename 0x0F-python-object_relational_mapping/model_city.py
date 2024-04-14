#!/usr/bin/python3
"""this will defines the city  class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from model_state import Base


class City(Base):
    """this defines ORM class for table
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
