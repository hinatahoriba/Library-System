import sqlite3
import datetime
import init_database

data = [(9780123456789, 1001, datetime.date.today(), None)]
init_database.insert("status", data)
init_database.select("status")