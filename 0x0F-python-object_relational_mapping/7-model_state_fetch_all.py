#!/usr/bin/python3

""" This is a script that lists all state object from hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    content = 'mysql+mysqldb://{}:{}@localhost/{}'\
                .format(argv[1], argv[2], argv[3])
    engine = create_engine(content, pool_pre_ping=True)
    Base.metadata.create_all(engine)

session = Session(engine)
states = session.query(State).all()

for state in states:
    print("{}: {}".format(state.id, state.name))
    session.close()
