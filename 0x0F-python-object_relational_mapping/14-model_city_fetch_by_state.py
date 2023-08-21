#!/usr/bin/python3
"""
define a script that list all states"""
import sys as f
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(f.argv[1], f.argv[2],
                f.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ss = Session()
    c_r = ss.query(City, State).\
        filter(City.state_id == State.id).all()
    for c, st in c_r:
        print("{}: ({}) {}".format(st.name, c.id, c.name))
    ss.commit()
    ss.close()
