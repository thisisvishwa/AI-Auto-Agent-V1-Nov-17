```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    transaction_schema = Column(String)

class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    wallet_schema = Column(String)

class SmartContract(Base):
    __tablename__ = 'smart_contracts'

    id = Column(Integer, primary_key=True)
    smart_contract_schema = Column(String)

class DatabaseInstance:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def data_storage(self, data, table):
        session = self.Session()
        session.add(table(**data))
        session.commit()

    def data_retrieval(self, table):
        session = self.Session()
        return session.query(table).all()

database_instance = DatabaseInstance('sqlite:///ai_agent.db')
database_instance.create_tables()
```