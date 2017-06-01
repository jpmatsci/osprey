import sqlite3 as sql


class dotdict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value

class ospdb:

    def __init__(self, database):
        self.database = database
        self.db = sql.connect(database)

    def openread(self, query):
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
        for row in self.openread('DESCRIBE '+table):
            #row[0] is the header, row[1] is the description
            headers.append(row[0])
        return headers

    def dictrow(self, table, ident):
            headers = self.get_headers(table)
            response = {header : self.get_item_from_table('select '+header+' from '+table+' where id='+str(ident)) for header in headers}
            return response

    def put_command(self, command):
        try:
            self.db.execute(command)
            self.db.commit()
            return True
        except self.db.Error as err:
            print err
            return False

