#!/usr/bin/python3
"""
that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (s_name_searched,))
    rs = cur.fetchall()
    for r in rs:
        print(r)
    cur.close()
    db.close()
