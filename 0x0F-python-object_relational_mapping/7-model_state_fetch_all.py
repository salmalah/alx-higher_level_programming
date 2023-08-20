#!/usr/bin/python3
"""
define a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys as y
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u_name = y.argv[1]
    pass_d = y.argv[2]
    db_name = y.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        u_name, pass_d, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ss = Session()
    states = ss.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    ss.close()
