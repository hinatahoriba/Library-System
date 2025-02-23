import sqlite3
import datetime

dbname = "library_system.db"

def create(table, *columns):
    with sqlite3.connect(dbname) as con:
        cursor = con.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table}({','.join(columns)})")

def insert(table, data):
    with sqlite3.connect(dbname) as con:
        cursor = con.cursor()
        try:
            cursor.executemany(f"INSERT INTO {table} VALUES(?, ?, ?, ?)", data)
        except sqlite3.IntegrityError as e:
            print(f"{e}が発生しました")
  
# for row in cur.execute("SELECT * FROM status WHERE return_date IS NULL"):      
def select(table):
    with sqlite3.connect(dbname) as con:
        cursor = con.cursor()
        print("-" * 20)
        print(f"This is {table}")
        for row in cursor.execute(f"SELECT * FROM {table}"):
            print(row)
        print()

"""
def update(table, column, value, ):
    with sqlite3.connect(dbname) as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE {table} SET )")
"""

if __name__ == '__main__': 
    # usersテーブルのテストデータ
    users_data = [
        (1001, 'John Smith', datetime.date(2024, 9, 1), datetime.date(2025, 2, 23)),
        (1002, 'Emma Johnson', datetime.date(2024, 9, 2), datetime.date(2025, 2, 23)),
        (1003, 'Michael Brown', datetime.date(2024, 9, 3), datetime.date(2025, 2, 23)),
        (1004, 'Sophia Davis', datetime.date(2024, 9, 4), datetime.date(2025, 2, 23)), 
        (1005, 'William Wilson', datetime.date(2024, 9, 5), datetime.date(2025, 2, 23))
    ]

    # bookテーブルのテストデータ
    book_data = [
        (9780123456789, 1, datetime.date(2024, 10, 1), datetime.date(2025, 2, 23)),
        (9780234567890, 2, datetime.date(2024, 10, 2), datetime.date(2025, 2, 23)),
        (9780345678901, 3, datetime.date(2024, 10, 3), datetime.date(2025, 2, 23)),
        (9780456789012, 4, datetime.date(2024, 10, 4), datetime.date(2025, 2, 23)),
        (9780567890123, 5, datetime.date(2024, 10, 5), datetime.date(2025, 2, 23))
    ]

    # statusテーブルのテストデータ
    status_data = [
        (9780123456789, 1001, datetime.date(2025, 2, 1), datetime.date(2025, 2, 15)),
        (9780234567890, 1002, datetime.date(2025, 2, 5), None),
        (9780345678901, 1003, datetime.date(2025, 2, 10), None),
        (9780456789012, 1004, datetime.date(2025, 2, 15), None),
        (9780567890123, 1005, datetime.date(2025, 2, 20), None)
    ]

    # テーブルを作成している
    create("users", "student_id INTEGER PRIMARY KEY", "name TEXT NOT NULL", "signup_at DATE NOT NULL", "updated_at")
    create("book", "isbn INTEGER PRIMARY KEY", "book_num INTEGER NOT NULL", "signup_at DATE NOT NULL","updated_at")
    create("status", "isbn INTEGER", "student_id INTERGER", "lend_date DATE NOT NULL", "return_date")
    # データを登録している
    insert("users", users_data)
    insert("book", book_data)
    insert("status", status_data)
    # ちゃんと作成できているか確認
    select("users")
    select("book")
    select("status")