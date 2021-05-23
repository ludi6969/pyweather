import sqlite3
import utils

class Db:
    def __init__(self, path):
        self.__db = sqlite3.connect(path, isolation_level=None)
        self.__dbcur = self.__db.cursor()

    def init(self):
        self.__dbcur.execute('''CREATE TABLE measures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date STRING,
            temperature STRING,
            downfall STRING
        );''')

    def insert(self, temp, downfall):
        self.__dbcur.execute('''INSERT INTO measures (date, temperature, downfall) VALUES (
            '%s', '%s', '%s' );''' % (utils.get_current_datetime(), temp, downfall))

    def get_all(self):
        return self.__dbcur.execute('''SELECT * FROM measures ORDER BY id DESC''').fetchall()

    def get(self, limit):
        return self.__dbcur.execute('''SELECT * FROM measures ORDER BY id DESC LIMIT %d''' % limit).fetchall()
    
    def count(self):
        return self.__dbcur.execute('''SELECT COUNT(id) FROM measures''').fetchone()[0]

    def close(self):
        return self.__db.close()
