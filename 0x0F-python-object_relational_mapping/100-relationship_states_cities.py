#!/usr/bin/python3
"""
Script creates the State "California" with the City "San Francisco" from the database
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="California")
    session.add(newState)
    session.commit()
    """newCity = City(name="San Francisco", state="California")
    session.add(newCity)
    session.commit()
    session.close()"""
