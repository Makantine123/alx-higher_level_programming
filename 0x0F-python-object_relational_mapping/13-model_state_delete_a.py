#!/usr/bin/python3
"""
Script deletes all the State objects with name
containing the letter 'a' from the database
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    if (len(argv)) != 4:
        exit()

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_a = session.query(State).filter(State.name.contains('%a%')).all()
    for state in state_a:
        session.delete(state)
    session.commit()
    session.close()
