"""
A program that stores book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
import BookstoreBackend

window=Tk()

window.wm_title("Bookstore")

def view_command():
    #Empty the list first
    list1.delete(0,END)
    #Iterate through the database
    for row in BookstoreBackend.view():
        list1.insert(END,row)

def search_command():
    #Empty the list first
    list1.delete(0,END)
    #Iterate through the database and search for ite
    for row in BookstoreBackend.search(
            title_text.get(),       #Output a string object for the title
            author_text.get(),      #Output a string object for author
            year_book.get(),        #Output a string object for year of the book
            isbn_number.get()):     #Output a string object for the isbn number
        list1.insert(END,row)       #Insert values at the end of the list

def add_command():
    BookstoreBackend.insert(title_text.get(),author_text.get(),year_book.get(),isbn_number.get())
    list1.delete(0,END)
    #Display in the listbox the added book
    list1.insert(END,(title_text.get(),author_text.get(),year_book.get(),isbn_number.get()))

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])

def delete_command():
    BookstoreBackend.delete(selected_tuple[0])

def update_command():
    BookstoreBackend.update(selected_tuple[0],
                            title_text.get(),
                            author_text.get(),
                            year_book.get(),
                            isbn_number.get())

#Label Fields
l1=Label(window,text="Title")
l1.grid(row=1,column=0)

l2=Label(window,text="Author")
l2.grid(row=1,column=2)

l3=Label(window,text="Year")
l3.grid(row=2,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=2,column=2)

#Entry Fields
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=1,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=3)

year_book=StringVar()
e3=Entry(window,textvariable=year_book)
e3.grid(row=2,column=1)

isbn_number=StringVar()
e4=Entry(window,textvariable=isbn_number)
e4.grid(row=2,column=3)

#Listbox to display all books
list1=Listbox(window, height=6,width=35)
list1.grid(row=3,column=0, rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

#Scrollbar for listbox
sb1=Scrollbar(window)
sb1.grid(row=5, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Button Controls
b1=Button(window,text="Viewall", width=12, command=view_command)
b1.grid(row=4, column=3)

b2=Button(window,text="Search Entry", width=12, command=search_command)
b2.grid(row=5, column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=6, column=3)

b4=Button(window,text="Update", width=12, command=update_command)
b4.grid(row=7, column=3)

b5=Button(window,text="Delete", width=12, command=delete_command)
b5.grid(row=8, column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=9, column=3)

window.mainloop()