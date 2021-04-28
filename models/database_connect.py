from sqlite3 import Connection
import os

path = os.getcwd()

path_database = (path[:path.rindex("\\")] + '\\database\\database_test.db')
conn = Connection(path_database)

cur = conn.cursor()

