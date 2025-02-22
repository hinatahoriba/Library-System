import sqlite3
from datetime import date

isbn = 9780123456789
student_id = 1001
lend_date = date.today().strftime("%Y-%m-%d")
return_date = date.today().strftime("%Y-%m-%d")
dbname = "library_system.db"
with sqlite3.connect(dbname) as con:
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO status VALUES({isbn}, {student_id}, {lend_date}, {return_date})")
    
with sqlite3.connect(dbname) as con:
    cursor = con.cursor()
    for row in cursor.execute(f"SELECT * FROM status"):
            print(row)