#This is the osprey database setup script
#the database goes into the folder
#the script is run in

#Generate path for database in this folder
import sys, os
wd = os.getcwd()+'/'
dbstr = 'sqlite:///'+wd+'ospdb.db'

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Table, Column, Date, Integer, String, MetaData, ForeignKey

engine = create_engine(dbstr, echo=True)
metadata = MetaData()

#add auto increment to id below!!!!
articles = Table("articles", metadata,
Column('id', Integer, primary_key=True),
Column('date',Date),    #this will be the creation date
Column('title', String),
Column('description', String),  #This will be a short description for its parent to show
Column('content', String),  #the html for the page will be saved here
Column('parentid', Integer),
)

metadata.create_all(engine)
