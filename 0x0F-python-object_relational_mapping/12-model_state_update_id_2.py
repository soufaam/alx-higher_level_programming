#!/usr/bin/python3
"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """The entry point where the script will executed"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:13306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    factory = sessionmaker(bind=engine)
    session = factory()
    result = session.query(State).filter(State.id == 2)
    record = result.one()
    record.name = "New Mexico"
    session.commit()
