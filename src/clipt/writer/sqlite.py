import sqlite3

class SqliteWriter:

    def __init__(self, db_path):
        self._db = sqlite3.connect(db_path)

        self._db.execute('''CREATE TABLE IF NOT EXISTS clips
        (key text, value text)''')

    def write(self, key, value):
        sql = 'INSERT INTO clips (key, value) VALUES (?, ?)'
        self._db.execute(sql, (key, value))

    def read(self, key):
        sql = "SELECT value FROM clips WHERE key = ?"
        result = self._db.execute(sql, (key,))

        result = result.fetchone()
        if result != None:
            return result[0]

    def list(self):
        sql = "SELECT key FROM clips"
        result = self._db.execute(sql)
        return result.fetchall()
