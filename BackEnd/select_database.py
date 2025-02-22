def display_all(table_name):
    import sqlite3
    con = sqlite3.connect("library_system.db")
    cur = con.cursor()
    print("-" * 20)
    print(f"以下は{table_name}")
    for row in cur.execute(f"SELECT * FROM {table_name}"):
        print(row)
    print()
    con.close()

def display():
    import sqlite3
    con = sqlite3.connect("library_system.db")
    cur = con.cursor()
    print("-" * 20)
    print("以下は他の人が借りている本です。")
    for row in cur.execute("SELECT * FROM status WHERE return_date IS NULL"):
        print(row)
    print()
    con.close()
    
display_all("users")
display_all("book")
display_all("status")
display()