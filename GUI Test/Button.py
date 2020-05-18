from tkinter import *

root = Tk()
b1 = Button(text="Изменить", width=15, height=3)


def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'


b1.config(command=change)

b1.pack()
root.mainloop()