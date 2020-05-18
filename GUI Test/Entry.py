from tkinter import *
root = Tk()
e1 = Entry(width=50)
def insert():
    e1.insert(0,"Tkinter - GUI Test ")
b = Button(text="Вставить", command=insert)
e1.pack()
b.pack()
root.mainloop()