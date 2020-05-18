
from tkinter import *
root = Tk()

Label(text="Имя кккккк:\nИ название").grid(row=0, column=0, sticky=W+E, pady=50, padx=10)
# Label(text="Имя:").grid(row=0, column=1, sticky=W+E, pady=50, padx=10)
# Label(text="Имя:").grid(row=0, column=2, sticky=W+E, pady=50, padx=10)
# Label(text="Имя:").grid(row=0, column=3, sticky=W+E, pady=50, padx=10)
# Label(text="Имя:").grid(row=0, column=4, sticky=W+E, pady=50, padx=10)
# Label(text="Имя:").grid(row=0, column=5, sticky=W+E, pady=50, padx=10)
table_name = Entry()
table_name.grid(row=1, column=1, columnspan=3, sticky= W+E, padx=10)
# table_name.insert(0, "sdfsfsfdsdf\nsdfsfsdf\nssgsgsdgsdg\nsgsdg")
Label(text="Столбцов:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
table_column = Spinbox(width=7, from_=1, to=50)
table_column.grid(row=1, column=1, padx=10)
Label(text="Строк:").grid(row=1, column=2, sticky=E)
table_row = Spinbox(width=7, from_=1, to=100)
table_row.grid(row=1, column=3, sticky=E, padx=10)

# root.grid_columnconfigure(0, weight = 1)

Button(text="Справка").grid(row=2, column=0, pady=10, padx=10)
Button(text="Вставить").grid(row=2, column=2)
Button(text="Отменить").grid(row=2, column=3, sticky=N+W+S+E, padx=10)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())


root.columnconfigure(3, weight=1, minsize=450)
# root.rowconfigure(2, weight=1)

root.mainloop()