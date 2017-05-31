#**** warning this will erase your site if run*****

from utilities import ospdb
import sys

datab = ospdb('SITE')

datab.put_command('DROP TABLE PAGES')

page_info = """
CREATE TABLE IF NOT EXISTS PAGES (
ID INTEGER PRIMARY KEY,
TITLE TEXT,
BODY TEXT,
AUTHOR TEXT,
DATE DATETIME)
"""
if not datab.put_command(page_info):
    print "problem with page_info"
    sys.exit()

