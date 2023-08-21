#!/usr/bin/python3
"""
define a script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys as f
from sqlalchemy.orm import relationship
from relationship_city import City
from relationship_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u_name = f.argv[1]
    pass_d = f.argv[2]
    db_name = f.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(u_name, pass_d, db_name))
    Session = sessionmaker(bind=engine)
    ss = Session()
    s_q = ss.query(City).order_by(City.id)
    for c in s_q:
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
