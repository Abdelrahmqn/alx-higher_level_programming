#!/usr/bin/python3
"""Link Mysqlalchemy documentation by making a simple schema
"""

from sqlalchemy import Column, MetaData, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base(metadata=MetaData())


class State(Base):
    """class State Documentaion"""

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

