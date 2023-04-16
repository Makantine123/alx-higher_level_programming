#!/usr/bin/python3
"""
Script contains class definition of a City and an instance of
Base = declarative_base()
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base, State


class City(Base):
    """Class contains cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
