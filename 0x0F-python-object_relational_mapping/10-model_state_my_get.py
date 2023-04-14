#!/usr/bin/python3
"""Script that pribts the State object with name passed as argument
from database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == argv[4]).first()

    if (result):
        print("{}".format(result.id))
    else:
        print("Not found")
