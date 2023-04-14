#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from model_state import Base, State
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    result = db.cursor()
    result.execute("SELECT states.name, cities.id, cities.name\
                   FROM states join cities on states.id = cities.state_id\
                   ORDER BY cities.id ASC")

    for row in result.fetchall():
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
