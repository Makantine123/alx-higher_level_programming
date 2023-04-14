#!/usr/bin/python3
"""
Script lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    result = db.cursor()
    result.execute("""SELECT * FROM states
    WHERE name = '{}' ORDER BY id""".format(state_name))

    for row in result.fetchall():
        print("({}, {})".format(row[0], row[1]))
