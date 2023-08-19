from sqlalchemy import create_engine, MetaData, func, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

#database connection
engine = create_engine('sqlite:///trip_records.db')
Base = declarative_base()
#User class (table)
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    Email = Column(String())
    Phone = Column(String())
    created_at = Column(DateTime(),server_default=func.now())
    