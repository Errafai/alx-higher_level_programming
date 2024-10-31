#!/usr/bin/python3
"""Start link class to table in database"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    id_2 = session.query(State).filter_by(id=2).first()

    id_2.name = "New Mexico"

    session.commit()
