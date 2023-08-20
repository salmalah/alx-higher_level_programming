#!/usr/bin/python3
"""
define a  a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    u_name = sys.argv[1]
    pass_d = sys.argv[2]
    dab_name = sys.argv[3]
    s_name_searched = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         passwd=pass_d, db=dab_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (s_name_searched, ))
    rs = cur.fetchall()
    for r in rs:
        print(r)
    cur.close()
    db.close()
