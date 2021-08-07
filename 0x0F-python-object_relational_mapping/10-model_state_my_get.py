#!/usr/bin/python3
""" prints the state object with the name passed as an arguement"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    f_flag = 0
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            f_flag = 1
            break

    if f_flag == 0:
        print("Not found")
