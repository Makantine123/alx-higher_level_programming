#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)

    for row in result.all():
        print("{}: {}".format(row.id, row.name))
