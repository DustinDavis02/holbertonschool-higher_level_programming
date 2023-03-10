#!/usr/bin/python3
"""Filter states in hbtn_0e_0_usa when name matching argument"""

import MySQLdb
from sys import argv


def my_filter_states():
    """takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                .format(argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_filter_states()