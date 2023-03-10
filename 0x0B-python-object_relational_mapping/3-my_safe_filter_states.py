#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def my_filter_states():
    """takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
    but is safe from sql injections."""

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (argv[4], ))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_filter_states()