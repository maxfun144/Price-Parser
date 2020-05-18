from tkinter import Tk, Toplevel, Button, Label

# При помощи функции grab_set мы передаем поток данному виджету т.е. делаем его модальным(нельзя переключиться на главное окно).
#
# При помощи функции focus_set() мы фокусируем наше приложение на окне top, а при помощи функции wait_window() мы задаем приложению команду, что пока не будет закрыто окно top пользоваться другим окном будет нельзя.
# При помощи transient(root) можно убарть кнопки свернуть/развернуть, а так же расширить экран благодаря чему получим простое модальное диалоговое окно.

def func():
    top = Toplevel(root)
    button_top_level = Button(top, text='Нажми', command=lambda: label.config(text='Текст из модального окна')).pack()
    # button_top_level = Button(top, text='Нажми', command=destroy(top)).pack()
    top.transient(root)
    top.grab_set()
    top.focus_set()
    top.wait_window()

root = Tk()
label = Label(root, text='Текст')
label.pack()
button = Button(root, text='openModal', command=func).pack()
root.mainloop()