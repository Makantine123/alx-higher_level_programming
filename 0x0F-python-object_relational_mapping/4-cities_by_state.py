#!/usr/bin/python3
"""
Script that lists all the cities from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    result = db.cursor()
    result.execute("""SELECT c.id, c.name, s.name FROM cities c
    JOIN states s on s.id=c.state_id ORDER BY c.state_id""")

    for row in result.fetchall():
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
