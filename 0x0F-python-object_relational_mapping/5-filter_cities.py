#!/usr/bin/python3
"""
Script takes in the name of a state as an argument and lists all the cities
of that state.
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    state = argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    result = db.cursor()

    result.execute("""SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name=%s ORDER BY cities.id""", (state,))

    rows = result.rowcount
    count = 0

    for row in result.fetchall():
        count += 1
        print("{}".format(row[0]), end="")

        if (count < rows):
            print(", ", end="")
    print()
