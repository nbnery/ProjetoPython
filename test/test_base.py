from base.database import SessionLocal, engine
import base.table as table
from sqlalchemy_utils import database_exists, drop_database, get_columns
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
        self.tables = table.Base.metadata.tables.keys()

    def test_customer_table(self):
        assert 'customer' in self.tables
        assert len(get_columns(table.Customer)) == 4
        assert isinstance(table.Customer.id.type, table.Integer)
        assert isinstance(table.Customer.name.type, table.String)
        assert isinstance(table.Customer.cpf.type, table.String)
        assert isinstance(table.Customer.phone.type, table.String)

