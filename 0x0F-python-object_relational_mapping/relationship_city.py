#!/usr/bin/python3
"""Link Mysqlalchemy documentation by making a simple schema
    for cities.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """class city Documentaion"""

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
