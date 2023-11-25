#!/usr/bin/python3

""" This script lists all city objects from hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    content = 'mysql+mysqldb://{}:{}@localhost/{}'\
                .format(argv[1], argv[2], argv[3])
    engine = create_engine(content, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(City, State)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id)

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
