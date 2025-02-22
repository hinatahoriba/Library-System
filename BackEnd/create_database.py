import sqlite3
con = sqlite3.connect("Library/library_system.db")

cur = con.cursor()
cur.execute("CREATE TABLE users(student_id, name, signup_at, updated_at)")
cur.execute("CREATE TABLE book(isbn, number, signup_at, updated_at)")
cur.execute("CREATE TABLE status(isbn, student_id, lend_date, return_date)")

con.commit()
con.close()
