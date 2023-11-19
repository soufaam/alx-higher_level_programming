#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    factory = sessionmaker(bind=engine)
    session = factory()
    idx = 1
    for instance in session.query(State).filter_by(id=1):
        print("{}: {}".format(idx, instance.name))
        idx += 1
