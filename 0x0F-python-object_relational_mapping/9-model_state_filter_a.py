#!/usr/bin/python3
"""
define a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""
import sys as f
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    u_name = f.argv[1]
    pass_d = f.argv[2]
    db_name = f.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(u_name, pass_d, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ss = Session()
    for st in ss.query(State).order_by(State.id):
        if "a" in st.name:
            print("{}: {}".format(st.id, st.name))
