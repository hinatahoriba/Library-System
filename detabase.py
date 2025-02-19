# データベース作るファイル

import sqlite3

dbname = 'lablib.db'
sqlite3.connect(dbname)
conn = sqlite3.connect(dbname)
cur = conn.cursor()

users_table_sql = 'CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY, name TEXT, reg_date DATE, update_date DATE)'
cur.execute(users_table_sql)

books_table_sql = 'CREATE TABLE IF NOT EXISTS books (isbn INTEGER PRIMARY KEY, title TEXT, num INTEGER, reg_date DATE, update_date DATE)'
cur.execute(books_table_sql)

rent_table_sql = 'CREATE TABLE IF NOT EXISTS rent (user_id TEXT, isbn INTEGER, rent_date DATE, return_date DATE, PRIMARY KEY(user_id, isbn))' 
cur.execute(rent_table_sql)

# テーブルを削除する
#cur.execute('DROP TABLE users')
#cur.execute('DROP TABLE books')
#cur.execute('DROP TABLE rent')


conn.commit()
conn.close()
