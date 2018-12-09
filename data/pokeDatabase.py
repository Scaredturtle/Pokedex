import sqlite3
from sqlite3 import Error

class pokeData:
    def createDatabase(self, dbfile):
        print("got here")
        try:
            print("got this far")
            database = sqlite3.connect(dbfile)
        except Error as e:
            print(e)
        finally:
            database.close()