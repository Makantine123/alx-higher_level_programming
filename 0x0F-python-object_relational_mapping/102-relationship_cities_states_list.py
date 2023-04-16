#!/usr/bin/python3
"""
Script lists all City objects
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    myCities = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id).all()

    for city, state in myCities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
