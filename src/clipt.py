#!/usr/bin/env python3

from clipt.core.clipt import Clipt
from clipt.writer import sqlite

clipt = Clipt(sqlite.SqliteWriter(':memory:'))

clipt.write('poop', 'this is a value')

print(clipt.read('poop'))
