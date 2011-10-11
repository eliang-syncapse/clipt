import sqlite3

from clipt.writer import writer

dir(writer)
class SqliteWriter(writer.Writer):

    def __init__(self, db_path):
        self._db = sqlite3.connect(db_path)

        self._db.execute('''CREATE TABLE IF NOT EXISTS clips
        (key text, value text)''')

    def write(self, key, value):
        self._db.execute('''REPLACE INTO clips (key, value) 
        VALUES (?, ?)''', (key, value))

    def read(self, key):
        sql = "SELECT value FROM clips WHERE key = ?" 
        result = self._db.execute(sql, (key,))

        return result.fetchone()[0]


