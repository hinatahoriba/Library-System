import sqlite3
import datetime
import init_database

user_data = [(1006, 'Olivia Taylor', datetime.date.today(), None)]
init_database.insert("users", user_data)

book_data = [(9780678901234, 6, datetime.date.today(), None)]
init_database.insert("book", book_data)

init_database.select("users")
init_database.select("book")