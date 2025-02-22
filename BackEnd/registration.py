import sqlite3

# データベースにデータを登録する
def registeration(table, date):
    con = sqlite3.connect("library_system.db")
    cur = con.cursor()
    cur.executemany(f"INSERT INTO {table} VALUES(?, ?, ?, ?)", date)
    con.commit()
    con.close()

# users テーブルのテストデータ
users_data = [
    (1001, "佐藤太郎", "2024-01-15 10:30:00", "2024-01-15 10:30:00"),
    (1002, "鈴木花子", "2024-01-16 11:45:00", "2024-01-16 11:45:00"),
    (1003, "田中一郎", "2024-01-17 09:15:00", "2024-01-17 09:15:00"),
    (1004, "山田優子", "2024-01-18 14:20:00", "2024-01-18 14:20:00"),
    (1005, "伊藤健太", "2024-01-19 16:00:00", "2024-01-19 16:00:00"),
    (1006, "渡辺美咲", "2024-01-20 10:10:00", "2024-01-20 10:10:00"),
    (1007, "小林竜也", "2024-01-21 13:30:00", "2024-01-21 13:30:00"),
    (1008, "加藤恵", "2024-01-22 15:45:00", "2024-01-22 15:45:00"),
    (1009, "吉田翔太", "2024-01-23 11:20:00", "2024-01-23 11:20:00"),
    (1010, "中村愛", "2024-01-24 12:00:00", "2024-01-24 12:00:00"),
    (1011, "森田光", "2024-01-25 09:50:00", "2024-01-25 09:50:00"),
    (1012, "高橋誠", "2024-01-26 14:15:00", "2024-01-26 14:15:00")
]

# book テーブルのテストデータ
book_data = [
    ("978-4-1234-5678-9", "B001", "2024-01-01 08:00:00", "2024-01-01 08:00:00"),
    ("978-4-2345-6789-0", "B002", "2024-01-02 09:30:00", "2024-01-02 09:30:00"),
    ("978-4-3456-7890-1", "B003", "2024-01-03 10:45:00", "2024-01-03 10:45:00"),
    ("978-4-4567-8901-2", "B004", "2024-01-04 11:15:00", "2024-01-04 11:15:00"),
    ("978-4-5678-9012-3", "B005", "2024-01-05 13:20:00", "2024-01-05 13:20:00"),
    ("978-4-6789-0123-4", "B006", "2024-01-06 14:40:00", "2024-01-06 14:40:00"),
    ("978-4-7890-1234-5", "B007", "2024-01-07 15:50:00", "2024-01-07 15:50:00"),
    ("978-4-8901-2345-6", "B008", "2024-01-08 16:30:00", "2024-01-08 16:30:00"),
    ("978-4-9012-3456-7", "B009", "2024-01-09 09:10:00", "2024-01-09 09:10:00"),
    ("978-4-0123-4567-8", "B010", "2024-01-10 10:25:00", "2024-01-10 10:25:00"),
    ("978-4-1234-5678-0", "B011", "2024-01-11 11:40:00", "2024-01-11 11:40:00"),
    ("978-4-2345-6789-1", "B012", "2024-01-12 13:55:00", "2024-01-12 13:55:00")
]

# status テーブルのテストデータ
status_data = [
    ("978-4-1234-5678-9", 1001, "2024-02-01", "2024-02-15"),
    ("978-4-2345-6789-0", 1002, "2024-02-02", "2024-02-16"),
    ("978-4-3456-7890-1", 1003, "2024-02-03", "2024-02-17"),
    ("978-4-4567-8901-2", 1004, "2024-02-04", "2024-02-18"),
    ("978-4-5678-9012-3", 1005, "2024-02-05", "2024-02-19"),
    ("978-4-6789-0123-4", 1006, "2024-02-06", "2024-02-20"),
    ("978-4-7890-1234-5", 1007, "2024-02-07", "2024-02-21"),
    ("978-4-8901-2345-6", 1008, "2024-02-08", "2024-02-22"),
    ("978-4-9012-3456-7", 1009, "2024-02-09", None),
    ("978-4-0123-4567-8", 1010, "2024-02-10", None),
    ("978-4-1234-5678-0", 1011, "2024-02-11", None),
    ("978-4-2345-6789-1", 1012, "2024-02-12", None)
]

#テストデータの追加
registeration("users", users_data)
registeration("book", book_data)
registeration("status", status_data)