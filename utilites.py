import sqlite3 as sql

#This is a small class allowing you to use dots
#in dictionaries for example:
#
# >>> variable['first'] = 1
# >>> print variable.first
#     1

class dotdict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value

#This is my main sqlite database class

class ospdb:

    def __init__(self, database):
        self.database = database
        self.db = sql.connect(database)

    def iter_query(self, query):
    #main query function, also a generator
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            #print query #for debugging                                  
            newrow = cursor.fetchone()
            while newrow:
                yield newrow
                newrow = cursor.fetchone()
        except mysql.connector.Error as err:
            print "Something went wrong: ", err.msg
            print "query was: ", query

    def get_headers(self, table):
        headers = []
        for row in self.iter_query('DESCRIBE '+table):
            headers.append(row[0])
        return headers

    def dictrow(self, table, key):
            headers = self.get_headers(table)
            response = {header : self.iter_query('select '+header+' from '+table+' where [PrimaryKey]='+str(key)) for header in headers}
            return response

    def put_command(self, command):
        try:
            self.db.execute(command)
            self.db.commit()
            return True
        except self.db.Error as err:
            print err
            return False
