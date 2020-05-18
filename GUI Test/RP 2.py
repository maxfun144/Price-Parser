import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        b = tk.Button(master=frame, text=f"Row {i}\nColumn {j}")
        b.pack()

window.mainloop()
