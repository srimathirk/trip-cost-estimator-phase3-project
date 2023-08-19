from sqlalchemy import create_engine, MetaData, func, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

#to maintain consistency of database schema
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
#database connection
engine = create_engine('sqlite:///trip_records.db')
# Base = declarative_base()

#creating association table
trip_user = Table(
    'trip_users',
    Base.metadata,
    Column('trip_id',ForeignKey('trips.trip_id'),primary_key=True),
    Column('user_id',ForeignKey('users.user_id'),primary_key=True)
)
expense_trip = Table(
    'expense_trips',
    Base.metadata,
    Column('expense_id',ForeignKey('expenses.expense_id'),primary_key=True),
    Column('trip_id',ForeignKey('trips.trip_id'),primary_key=True)
)
#User class (table)
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    Email = Column(String())
    Phone = Column(String())
    created_at = Column(DateTime(),server_default=func.now())
    trips = relationship("Trip", back_populates='user')
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
    expenses = relationship('Expense', back_populates='trip')
    user = relationship('User', back_populates='trips')
    def __repr__(self):
        return f'{self.trip_id} starts from {self.start_place} ends at {self.destination_place} has gas price {self.gas_cost} mileage:{self.mileage}'


#Expense class (table)
class Expense(Base):
    __tablename__='expenses'
    expense_id = Column(Integer(),primary_key=True)
    trip_id=Column(Integer(),ForeignKey('trips.trip_id'))
    cost_category = Column(String())
    amount = Column(Float())
    trip = relationship('Trip',back_populates='expenses')
    def __repr__(self):
        return f'{self.expense_id} whose trip{self.trip_id} category {self.cost_category} has price {self.amount}'
