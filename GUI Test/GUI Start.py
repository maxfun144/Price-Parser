from tkinter import *

root = Tk()

startButton = Button(text="Запустить программу.", width=30, height=3)
startButton.grid(row=0, column=0, sticky=W)

reportHeader = Label(text="Результат работы программы:", width=30, height=3)
reportHeader.grid(row=1, column=0, sticky=W)

reportText = Text()
reportText.grid(row=2, column=0, sticky=E+W+N+S)

root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)


w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 200
root.geometry('400x400+{}+{}'.format(w, h))

# root.resizable(False, False)
root.title("Главное окно")

root.mainloop()