#!/usr/bin/python3
"""Prints all `City` objects from the database `hbtn_0e_6_usa`"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id)):
        print(obj[0] + ": (" + str(obj[1]) + ") " + obj[2])
