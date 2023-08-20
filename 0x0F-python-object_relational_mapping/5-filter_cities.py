#!/usr/bin/python3
"""
define a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    u_name = sys.argv[1]
    pass_d = sys.argv[2]
    dab_name = sys.argv[3]
    s_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         passwd=pass_d, db=dab_name)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (s_name, ))
    rs = cur.fetchall()
    print(", ".join(map(lambda x: x[0], rs)))
    cur.close()
    db.close()
