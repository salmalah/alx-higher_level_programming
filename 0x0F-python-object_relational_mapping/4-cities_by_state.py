#!/usr/bin/python3
"""
define a script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    rs = cur.fetchall()
    for r in rs:
        print(r)
    cur.close()
    db.close()
