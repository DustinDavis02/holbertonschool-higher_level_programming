#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()