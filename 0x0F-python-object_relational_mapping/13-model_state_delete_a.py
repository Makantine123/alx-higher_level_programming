#!/usr/bin/python31
"""
Script deletes all the State objects with name
containing the letter 'a' from the database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like("%a%")).all()

    for record in result:
        session.delete(record)

    session.commit()

    session.close()
