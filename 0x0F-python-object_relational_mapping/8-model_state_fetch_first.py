#!/usr/bin/python3
"""
define a script that prints the first State object from the
database hbtn_0e_6_usa
"""
import sys as f
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u_name = f.argv[1]
    pass_d = f.argv[2]
    db_name = f.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        u_name, pass_d, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ss = Session()
    first_s = ss.query(State).order_by(State.id).first()
    if first_s:
        print("{}: {}".format(first_s.id, first_s.name))
    else:
        print("Nothing")
    ss.close()
