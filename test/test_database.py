from base.database import SessionLocal, engine
from base.table import Base
from sqlalchemy_utils import database_exists, drop_database
from sqlalchemy.orm.session import Session


class TestDatabase:
    def setup_class(cls):
        if database_exists(engine.url):
            drop_database(engine.url)
        Base.metadata.create_all(engine)

    def test_create_databse(self):
        assert database_exists(engine.url) == True

    def test_session(self):
        session = SessionLocal()
        assert isinstance(session, Session)
        session.close()

