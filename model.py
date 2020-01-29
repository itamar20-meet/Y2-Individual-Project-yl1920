from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
   __tablename__ = 'User'
   Id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)

		
class Hero(Base):
   __tablename__ = 'Hero'
   Id = Column(Integer, primary_key=True)
   name = Column(String)
   votes = Column(Integer)
