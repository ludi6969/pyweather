import sqlite3

class Db:
    def __init__(self, path):
        self.__db = sqlite3.connect(path)

    def init(self):
        self.__db.execute('''CREATE TABLE measures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            downfall REAL
        )''')

a = Db('./db.db')
a.init()
