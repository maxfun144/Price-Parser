from tkinter import *

root = Tk()


label = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))
label.grid(row=0, column=0, sticky=W)

text = Text()
text.grid(row=1, column=0, sticky=E+W+N+S)
string = "sdsfgdgdfgdfdoijsoijg;dsjgkdjsg;\nlkfldkglkdh;lkdglkd;hlfjlk\ndgjhlkdgk;;;;g;fjh;lk\nghgfffffffffffffffv\nffffffffff\nffffffff"
text.insert(1.0, string)

text.config(state=DISABLED)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()