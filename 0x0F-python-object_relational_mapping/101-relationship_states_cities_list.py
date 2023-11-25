#!/usr/bin/python3
"""
This list all State and coreesponding City in the DB
"""
import sys
from sqlalchemy import create_engine as e
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = e("mysql+mysqldb://{}:{}@localhost/{}"
               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
               pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
