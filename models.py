from sqlalchemy import Column,Integer,String,Float,ForeignKey
from app.database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    email=Column(String)

class Subscription(Base):
    __tablename__='subscriptions'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    plan=Column(String)
    status=Column(String)

class Payment(Base):
    __tablename__='payments'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    amount=Column(Float)
    status=Column(String)
