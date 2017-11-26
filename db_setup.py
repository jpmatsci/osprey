#This is the osprey database setup script
#all it does is make 2 tables in sqlite3
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

articles = Table("articles", metadata,
Column('id', Integer, primary_key=True),
Column('date',Date),
Column('title', String),
Column('content', String),
Column('sectionid', Integer),
)

sections = Table("sections", metadata,
Column('id', Integer, primary_key=True),
Column('title', String),
Column('content', String),
Column('type', String),
)

metadata.create_all(engine)
