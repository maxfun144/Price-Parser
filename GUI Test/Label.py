from tkinter import *
root = Tk()
l1 = Label(text="Машинное обучение\nHahaha", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()