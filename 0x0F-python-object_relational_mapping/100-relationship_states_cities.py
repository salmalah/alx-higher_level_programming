#!/usr/bin/python3
"""
define a a script that creates the State “California” with the
City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys as f
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    u_name = f.argv[1]
    pass_d = f.argv[2]
    db_name = f.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(u_name, pass_d, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ss = Session()
    ss.add(City(name="San Francisco", state=State(name="California")))
    ss.commit()
