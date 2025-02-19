# 操作を定義するファイル

import sqlite3
import json
import datetime
import xmltodict
import urllib

# 本

# 本を登録する
def register_book(isbn, num):
    # 接続
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    title = get_bookinfo(isbn)
    date = datetime.datetime.today()
    
    sql = 'INSERT INTO books (isbn, title, num, reg_date) VALUES (?, ?, ?, ?)'
    cur.execute(sql, (isbn, title, num, date))
    conn.commit()
    conn.close()
    
# 本を更新する
def update_book(isbn, num):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    date = datetime.datetime.today()
    
    sql = 'UPDATE books SET num = ?, update_date = ? WHERE isbn = ?'
    cur.execute(sql, (num, date, isbn))
    conn.commit()
    conn.close()
    
# 本を削除する
def delete_book(isbn):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    sql = 'DELETE FROM books WHERE isbn = ?'
    cur.execute(sql, (isbn,))
    conn.commit()
    conn.close()

# ユーザ

# ユーザを登録する
def register_user(user_id, name):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    date = datetime.datetime.today()
    
    sql = 'INSERT INTO users (user_id, name, reg_date) VALUES (?, ?, ?)'
    cur.execute(sql, (user_id, name, date))
    conn.commit()
    conn.close()
    
# ユーザを更新する
def update_user(user_id, name):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    date = datetime.datetime.today()
    
    sql = 'UPDATE users SET name = ?, update_date = ? WHERE user_id = ?'
    cur.execute(sql, (name, date, user_id))
    conn.commit()
    conn.close()
    
# ユーザを削除する
def delete_user(user_id):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    sql = 'DELETE FROM users WHERE user_id = ?'
    cur.execute(sql, (user_id,))
    conn.commit()
    conn.close()
    
# 貸借

# 借りる
def rent_book(user_id, isbn):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    date = datetime.datetime.today()
    sql = 'INSERT INTO rent (user_id, isbn, rent_date) VALUES (?, ?, ?)'
    cur.execute(sql, (user_id, isbn, date))
    conn.commit()
    conn.close()
    
# 返す
def return_book(user_id, isbn):
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    date = datetime.datetime.today()
    sql = 'UPDATE rent SET return_date = ? WHERE user_id = ? AND isbn = ?'
    cur.execute(sql, (date, user_id, isbn))
    conn.commit()
    conn.close()
    
# 検索

# 全ての本を検索する
def search_books():
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    sql = 'SELECT title FROM books'
    cur.execute(sql)
    books = cur.fetchall()
    conn.close()
    return books

# 全てのユーザを検索する
def search_users():
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    sql = 'SELECT name FROM users'
    cur.execute(sql)
    users = cur.fetchall()
    conn.close()
    return users


# 貸し出し中のほんを検索する
def search_rent_books():
    conn = sqlite3.connect('lablib.db')
    cur = conn.cursor()
    
    sql = 'SELECT users.name, books.title, rent.rent_date FROM rent join books on rent.isbn = books.isbn join users on rent.user_id = users.user_id WHERE return_date IS NULL'
    cur.execute(sql)
    rentaling = cur.fetchall()
    conn.close()
    return rentaling
    
# 本の情報を取得する
def get_bookinfo(isbn):
    url = f'http://iss.ndl.go.jp/api/opensearch?isbn={isbn}'
    urlopen = urllib.request.urlopen(url)
    bookdata = xmltodict.parse(urlopen.read().decode('utf-8'))
    title = bookdata['rss']['channel']['item']['title']
    return title
