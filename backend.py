import sqlite3

# SQLite does not have a storage class set aside for storing dates and/or times. 
# Instead, the built-in Date And Time Functions of SQLite are capable of storing 
# dates and times as TEXT, REAL, or INTEGER values:
# TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS"). 

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, date TEXT)")
    conn.commit()
    conn.close()


def insert(title, author, year, date):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, date))
    conn.commit()
    conn.close()  

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", date=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR date=?", (title, author, year, date))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, date):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, date=? WHERE id=?", (title, author, year, date, id))
    conn.commit()
    conn.close()  



connect()

# insert('Снеговик', 'Ю Несбе', 2011, '2020-06-11')
# delete(2)
#update(3, 'Тараканы', 'Ю Несбе', 2011, '2020-06-11')
#print(view())
#print(search(author="Ю Несбе"))