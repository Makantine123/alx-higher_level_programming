#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).\
        filter(State.id == City.state_id).\
        order_by(City.id).all()

    for row in result:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))

    session.close()
