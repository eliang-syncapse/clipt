import unittest

from clipt.core import clipt
from clipt.writer import sqlite

class TestClipt(unittest.TestCase):
    def test_read_and_write(self):
        myClipt = clipt.Clipt(sqlite.SqliteWriter(':memory:'))

        myClipt.write('my-key', 'this is a value')

        self.assertEqual(myClipt.read('my-key'), 'this is a value')
