import sqlite3

class Database:
    #Constructor or Initializer
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstores ("
                    "id INTEGER PRIMARY KEY,"
                    "title text,"
                    "year integer,"
                    "isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM bookstores")
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM bookstores WHERE"
                    "title=? OR"
                    "author=? OR"
                    "year=? OR"
                    "isbn=?,"
                    "(title,author,year,isbn)")
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM bookstores WHERE id=?",(id,))
        self.conn.commit()
        self.conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE bookstores SET "
                    "title=?, "
                    "author=?, "
                    "year=?, "
                    "isbn=? "
                    "WHERE id=?",
                    (title,author,year,isbn,id))

