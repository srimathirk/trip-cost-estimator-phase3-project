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
    trips = relationship("Trip", backref="user")
    def __repr__(self):
        return f'{self.user_id}. name: {self.user_name} email:{self.Email}, phone: {self.Phone} created_at:{self.created_at}'

#Trip class (table)
class Trip(Base):
    __tablename__='trips'
    trip_id = Column(Integer(),primary_key=True)
    start_place = Column(String())
    destination_place = Column(String())
    gas_cost = Column(Float())
    mileage = Column(Float())
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    #expense = relationship('Expense', backref="trip")
    user = relationship('User', backref="trip")
    def __repr__(self):
        return f'{self.trip_id} starts from {self.start_place} ends at {self.destination_place} has gas price {self.gas_cost} mileage:{self.mileage}'
