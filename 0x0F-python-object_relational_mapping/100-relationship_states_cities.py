#!/usr/bin/python3

""" This script filter states  and city relationship"""
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

    state_name = State(name="California")
    city_name = City(name="San Francisco", state=state_name)

    session.add(city_name)
    session.commit()
