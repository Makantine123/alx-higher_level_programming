#!/usr/bin/python3
"""
Script lists all states from the database hbtn_0e_0_usa
with a name starting with N (upper N)
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])
    result = db.cursor()
    result.execute("""SELECT id, name FROM states
                   WHERE (LEFT(name,1) = 'N') AND
                   (ASCII(LEFT(name,1)) BETWEEN 65 AND 90)""")

    for row in result.fetchall():
        print("({}, '{}')".format(row[0], row[1]))
