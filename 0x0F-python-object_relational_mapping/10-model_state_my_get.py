#!/usr/bin/python3
"""a script that prints the first State object
from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """The entry point where the script will executed"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    factory = sessionmaker(bind=engine)
    session = factory()
    param = sys.argv[4]
    results = session.query(State).filter(State.name == param).all()
    flag = False
    for result in results:
        flag = True
        print("{}".format(result.id))
    if not flag:
        print("Not found")
