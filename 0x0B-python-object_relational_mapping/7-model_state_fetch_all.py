#!/usr/bin/python3
"""list all states"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session(engine)
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}, {state.name}")
session.close()