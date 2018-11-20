import sqlite3

class Db():

    def __init__(self, db_path):
        self.conn = self.__connect(db_path)

    def __connect(self, db_name):
        return sqlite3.connect(db_name, check_same_thread=False)

    def getConn(self):
        return self.conn

    def getCursor(self):
        return self.conn.cursor()



db = Db('mynote.db')

def getConn():
    return db.getConn()

def getCursor():
    return db.getCursor()

