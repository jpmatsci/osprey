#**** warning this will erase your database if run*****
#
#This script should be run once when starting
#a new site to setup the database
#
#make the database "SITE" before running this

from utilities import sqldb
import sys

datab = sqldb('SITE')
#datab.put_command('DELETE TABLE ARTICLES') #for testing
#datab.put_command('DELETE TABLE SUBSECTIONS') #for testing

table_info = """
CREATE TABLE ARTICLES (
TITLE TEXT,
BODY TEXT,
HTML TEXT,
AUTHOR TEXT,
DATE DATETIME,
SUBSECTION INTEGER)
"""

if not datab.put_command(table_info):
    print "problem with setup"
    sys.exit()

table_info = """
CREATE TABLE SUBSECTIONS (
TITLE TEXT,
BODY TEXT,
HTML TEXT)
"""

if not datab.put_command(table_info):
    print "problem with setup"
    sys.exit()

