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

window=Tk()

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
list1=Listbox(window, height=6,width=25)
list1.grid(row=3,column=0, rowspan=6,columnspan=2)

#Scrollbar for listbox
sb1=Scrollbar(window)
sb1.grid(row=5, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Button Controls
b1=Button(window,text="Viewall", width=12)
b1.grid(row=4, column=3)

b2=Button(window,text="Search Entry", width=12)
b2.grid(row=5, column=3)

b3=Button(window,text="Add Entry", width=12)
b3.grid(row=6, column=3)

b4=Button(window,text="Update", width=12)
b4.grid(row=7, column=3)

b5=Button(window,text="Delete", width=12)
b5.grid(row=8, column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=9, column=3)

window.mainloop()