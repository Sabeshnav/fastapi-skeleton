from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from ..configs import Configs

configs = Configs()
engine = create_engine(configs.database.connection_string, pool_pre_ping=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)