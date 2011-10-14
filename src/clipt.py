#!/usr/bin/env python3
import argparse
import os

from clipt.core import clipt
from clipt.core import config
from clipt.writer import sqlite

configuration = config.ConfigLoader()

parser = argparse.ArgumentParser(description='Save and retrieve text snippets')
parser.add_argument('command', choices=('read', 'write', 'list', 'delete'))
parser.add_argument('key', help='Snippet name', nargs='?')
parser.add_argument('value', help='Snippet value to write', nargs='?')
args = parser.parse_args()

if not os.path.exists(configuration.home):
    os.mkdir(configuration.home)

handle = clipt.Clipt(sqlite.SqliteWriter(configuration.config['local']['database']))

if args.command == 'list':
    print('Snippets:')
    print(handle.list())
    for snippet in handle.list():
        print('    ' + snippet)

elif args.command == 'read':
    value = handle.read(args.key)
    if value != None:
        print(value)

elif args.command == 'write':
    handle.write(args.key, args.value)

