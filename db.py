# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3

conn = sqlite3.connect("orders")
curs = conn.cursor()

"""initialise table by reading sql in order"""
sql_file = open('./orders.sql')
sql_string = sql_file.read()
curs.executescript(sql_string)