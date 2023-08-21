#!/usr/bin/python3
"""
define a script that prints all City
objects from the database hbtn_0e_14_usa
"""
import sys as d
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u_name = d.argv[1]
    pass_d = d.argv[2]
    db_name = d.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        u_name, pass_d, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ss = Session()
    c_by_state = ss.query(City, State) \
         .filter(City.state_id == State.id) \
            .order_by(City.id)
    for st, c in c_by_state:
        print("{}: ({}) {}".format(c.name, c.id, st.name))
    ss.commit()
    ss.close()
