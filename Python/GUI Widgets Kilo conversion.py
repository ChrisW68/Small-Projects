from tkinter import *

window=Tk()

def kg_conversion():
    lbs=float(e2_value.get())*2.205
    t1.insert(END,lbs)

    grams=float(e2_value.get())*1000
    t2.insert(END,grams)

    ounces=float(e2_value.get())*35.274
    t3.insert(END,ounces)

b1=Button(window,text="Convert", command=kg_conversion)
b1.grid(row=2, column=0)

e1_value=Label(window,text="kg")
e1_value.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0, column=0)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=2)

t2=Text(window,height=1,width=10)
t2.grid(row=2,column=2)

t3=Text(window,height=1,width=10)
t3.grid(row=3,column=2)

window.mainloop()
