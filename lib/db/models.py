from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///trip_records.db')

Base = declarative_base()