#!/usr/bin/python3
"""
define a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    u_name = sys.argv[1]
    pass_d = sys.argv[2]
    dab_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         passwd=pass_d, db=dab_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rs = cur.fetchall()
    for r in rs:
        print(r)
    cur.close()
    db.close()
