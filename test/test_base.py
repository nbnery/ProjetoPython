from base.database import SessionLocal, engine
import base.table as table
from sqlalchemy_utils import database_exists, drop_database, get_tables
from sqlalchemy.orm.session import Session


class TestDatabase:
    def setup_class(cls):
        if database_exists(engine.url):
            drop_database(engine.url)
        table.Base.metadata.create_all(engine)

    def test_create_databse(self):
        assert database_exists(engine.url) == True

    def test_session(self):
        session = SessionLocal()
        assert isinstance(session, Session)
        session.close()

class TestTables:
    def setup_class(self):
        if database_exists(engine.url):
            drop_database(engine.url)
        table.Base.metadata.create_all(engine)

    def test_tables(self):
        tables = table.Base.metadata.tables.keys()
        assert 'customer' in tables 

    def test_type_columns_customer(self):
        assert isinstance(table.Customer.id.type, table.Integer)

 