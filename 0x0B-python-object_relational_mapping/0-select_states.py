#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb
    
if __name__ == "__main__":
    av = sys.argv
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=av[1], passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()