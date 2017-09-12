import sqlite3

class Database:

    def __init__():
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS bookstores ("
                    "id INTEGER PRIMARY KEY,"
                    "title text,"
                    "year integer,"
                    "isbn integer)")
        conn.commit()
        conn.close()

    def insert(title,author,year,isbn):
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def view():
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM bookstores")
        rows=cur.fetchall()
        conn.close()
        return rows

    def search(selftitle="",author="",year="",isbn=""):
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM bookstores WHERE"
                    "title=? OR"
                    "author=? OR"
                    "year=? OR"
                    "isbn=?,"
                    "(title,author,year,isbn)")
        rows=cur.fetchall()
        conn.close()
        return rows

    def delte(id):
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM bookstores WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(id,title,author,year,isbn):
        conn=sqlite3.connect("bookstore.db")
        cur=conn.cursor()
        cur.execute("UPDATE bookstores SET "
                    "title=?, "
                    "author=?, "
                    "year=?, "
                    "isbn=? "
                    "WHERE id=?",
                    (title,author,year,isbn,id))

