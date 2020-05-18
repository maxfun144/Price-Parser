import tkinter as tk
root = tk.Tk()
scrollbar = tk.Scrollbar(orient="horizontal")
e3 =tk.Entry(xscrollcommand=scrollbar.set)
e3.focus()
e3.pack(side="bottom",fill="x")
#e3.grid(row=10, column=7)
scrollbar.pack(fill="x")
scrollbar.config(command=e3.xview)
e3.config()

root.mainloop()