#!/usr/bin/python3
"""
Script contains class definition of a State and an instance of
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
