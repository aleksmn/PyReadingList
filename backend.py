import sqlite3

# SQLite does not have a storage class set aside for storing dates and/or times. 
# Instead, the built-in Date And Time Functions of SQLite are capable of storing 
# dates and times as TEXT, REAL, or INTEGER values:
# TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS"). 

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, date TEXT)")
        self.conn.commit()


    def insert(self, title, author, year, date):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, date))
        self.conn.commit()
  

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows


    def search(self, title="", author="", year="", date=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR date=?", (title, author, year, date))
        rows = self.cur.fetchall()
        return rows


    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()


    def update(self, id, title, author, year, date):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, date=? WHERE id=?", (title, author, year, date, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()



# insert('Снеговик', 'Ю Несбе', 2011, '2020-06-11')
# delete(2)
#update(3, 'Тараканы', 'Ю Несбе', 2011, '2020-06-11')
#print(view())
#print(search(author="Ю Несбе"))