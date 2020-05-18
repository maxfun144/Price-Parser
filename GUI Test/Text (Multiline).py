from tkinter import *

root = Tk()

text = Text(width=20, height=7)
text.pack(side=LEFT)
string = "sdsfgdgdfgdfdoijsoijg;dsjgkdjsg;\nlkfldkglkdh;lkdglkd;hlfjlk\ndgjhlkdgk;;;;g;fjh;lk\nghgfffffffffffffffv\nffffffffff\nffffffff"
text.insert(1.0, string)

text.config(state=DISABLED) # Read - only

# scroll = Scrollbar(command=text.yview)
# scroll.pack(side=LEFT, fill=Y)

# text.config(yscrollcommand=scroll.set)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)


root.mainloop()