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

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).\
        order_by(City.id)

    for row in result.all():
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
