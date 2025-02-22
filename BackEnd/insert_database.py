import sqlite3
con = sqlite3.connect("Library/library_system.db")
cur = con.cursor()

# usersテーブルのテストデータ
users_data = [
    (1001, '山田太郎', '2025-01-15 10:00:00', '2025-01-15 10:00:00'),
    (1002, '佐藤花子', '2025-01-16 11:30:00', '2025-01-16 11:30:00'),
    (1003, '鈴木一郎', '2025-01-17 09:15:00', '2025-01-17 09:15:00'),
    (1004, '田中美咲', '2025-01-18 14:45:00', '2025-01-18 14:45:00'),
    (1005, '高橋健太', '2025-01-19 16:20:00', '2025-01-19 16:20:00')
]

# bookテーブルのテストデータ
book_data = [
    ('978-4-06-519981-7', 5, '2025-01-10 09:00:00', '2025-01-10 09:00:00'),
    ('978-4-04-877801-8', 3, '2025-01-11 10:30:00', '2025-01-11 10:30:00'),
    ('978-4-08-703497-8', 7, '2025-01-12 11:45:00', '2025-01-12 11:45:00'),
    ('978-4-09-386592-7', 2, '2025-01-13 13:15:00', '2025-01-13 13:15:00'),
    ('978-4-06-294993-9', 4, '2025-01-14 15:00:00', '2025-01-14 15:00:00')
]

# statusテーブルのテストデータ
status_data = [
    ('978-4-06-519981-7', 1001, '2025-02-01', '2025-02-15'),
    ('978-4-04-877801-8', 1002, '2025-02-03', None),
    ('978-4-08-703497-8', 1003, '2025-02-05', '2025-02-19'),
    ('978-4-09-386592-7', 1004, '2025-02-07', None),
    ('978-4-06-294993-9', 1005, '2025-02-09', '2025-02-16')
]

cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", users_data)
cur.executemany("INSERT INTO book VALUES(?, ?, ?, ?)", book_data)
#cur.executemany("INSERT INTO status VALUES(?, ?, ?, ?)", status_data)

con.commit()
con.close()