#!/usr/bin/python3
"""Lists all state objects with lettr 'a'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


def a_state():
    """Lists State objects that contain letter 'a' from the database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    rows = session.query(State).all()
    for state in rows:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    a_state()