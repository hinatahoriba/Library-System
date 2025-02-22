import sqlite3
dbname = "library_system.db"
con = sqlite3.connect(dbname)

cur = con.cursor()
cur.execute("CREATE TABLE users(student_id, name, signup_at, updated_at)")
cur.execute("CREATE TABLE book(isbn, book_num, signup_at, updated_at)")
cur.execute("CREATE TABLE status(isbn, student_id, lend_date, return_date)")

con.commit()
con.close()
