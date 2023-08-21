#!/usr/bin/python3
"""
define a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""
import sys as f
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u_name = f.argv[1]
    pass_d = f.argv[2]
    db_name = f.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(u_name, pass_d, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ss = Session()
    s_q = ss.query(State).order_by(State.id)
    for st in s_q:
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("\t{}: {}".format(c.id, c.name))
