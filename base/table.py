from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Sequence, UniqueConstraint
from base.database import Base


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(300))
    cpf = Column(String(14), unique=True)
    phone = Column(String(12))

