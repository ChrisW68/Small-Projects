import sqlite3

#Connect to database function
def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstores "
                "(id INTEGER PRIMARY KEY, "
                "title text, "
                "author text, "
                "year integer, "
                "isbn integer)")
    conn.commit()
    #close the connection
    conn.close()

#Insert data into database function
def insert(title,author,year,isbn):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstores VALUES (null,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    #close the connection
    conn.close()

#View data into database function
def view():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstores")
    rows=cur.fetchall()
    #close the connection
    conn.close()
    return rows

#Search to find book information in database
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    #Want to find records in various search parameters
    #So I to be able to search for title or author or year or the isbn
    cur.execute("SELECT * FROM bookstores WHERE "
                "title=? "
                "OR author=? "
                "OR year=? "
                "OR isbn=?",
                (title,author,year,isbn))
    rows=cur.fetchall()
    #Close the connection
    conn.close()
    return rows

#Delete record in database
def delete(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookstores WHERE ID=?",(id,))
    conn.commit()
    #Close the connection
    conn.close()

#Update records in database
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
    conn.commit()
    #Close the connection
    conn.close()


connect()
#insert("The Wall","Bill Read",2010,1231231231)
#delete(4)
update(6,"The End of the World","Billy Bob",2005,1231254152)
print(view())
print(search(author="Bill Read"))