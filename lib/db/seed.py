#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Trip, Expense
import random
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
if __name__ == '__main__':
    #databasse connection
    engine = create_engine('sqlite:///trip_records.db')
    #Base.metadata.create_all(engine)

    #create a session
    Session = sessionmaker(bind=engine)
    session = Session()

#deleting old populated seed to make sure everything works fine
    session.query(User).delete()
    session.query(Trip).delete()
    session.query(Expense).delete()
    print("starting seed populates")
    session.commit()
#insert seed data
    names = ['John', 'Evan', 'Emma', 'Ana', 'Heshan', 'Shaan', 'Zoe', 'zia', 'rani', 'nila']
    #email = f'{names}@gmail.com'
    phones = ['5454545454', '3453453452', '1234123443', '6565657890']
    #start_date = datetime(2023, 1, 1)
    #end_date = datetime(2023, 12, 31)
    #time_difference = end_date - start_date
    #random_time = random.random()* time_difference.total_seconds()
            
    users = []
    for i in range (10):
        #random_seconds = random.randint(0,int(time_difference.total_seconds()))
        #random_time = start_date + timedelta(seconds=random_seconds)
        user = User(
            user_name=random.choice(names),
            Email=f'{random.choice(names)}@gmail.com',
            Phone=random.choice(phones),
            #created_at= random_time
        )
        # add and commit individually to get IDs back
        session.add(user)
        users.append(user)
    session.commit()

    start_places = ["NewYork", "NewJersey", "California", "niagarafalls US"]
    destination_places = ["Chicago", "Ohio", "Connecticut"]    
    
    trips=[]
    for i in range (10):
        trip= Trip(
            start_place=random.choice(start_places),
            destination_place=random.choice(destination_places),
            gas_cost=random.randint(10,555),
            mileage=random.randint(20,65)
        )
        session.add(trip)
        session.commit()
        trips.append(trip)
    categories = ["Food","Accomodation","entrance","parking"]
    expenses=[]
    for i in range (10):
        expense= Expense(
            cost_category=random.choice(categories),
            amount=random.randint(100,500)
        )
        session.add(expense)
        session.commit()
        expenses.append(expense)
    session.close()

# delete_records()
# create_user()
# create_trips()
# create_expenses()