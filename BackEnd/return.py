import sqlite3
dbname = "library_system.db"

with sqlite3.connect(dbname) as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE SET )")