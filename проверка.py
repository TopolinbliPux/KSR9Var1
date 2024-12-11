"""import tkinter as tk

def toggle_boundary_field(event):
    if step_option.get() == "Контроль выхода за границу":
        boundary_label.pack()
        boundary_entry.pack()
    else:
        boundary_label.pack_forget()
        boundary_entry.pack_forget()

# Создаем главное окно
root = tk.Tk()
root.title("Выбор опции")

# Заголовок
label = tk.Label(root, text="Выберите опцию:")
label.pack(pady=10)

# Переменная для хранения выбора
step_option = tk.StringVar(value="Определенное количество шагов")

# Выпадающий список
step_menu = tk.OptionMenu(root, step_option, "Определенное количество шагов", "Контроль выхода за границу")
step_menu.pack(pady=10)

# Поле для ввода количества шагов (по умолчанию)
steps_label = tk.Label(root, text="Введите количество шагов:")
steps_label.pack(pady=5)
steps_entry = tk.Entry(root)
steps_entry.pack(pady=5)

# Элементы для контроля выхода за границу, изначально скрыты
boundary_label = tk.Label(root, text="Контроль выхода за правую границу:")
boundary_entry = tk.Entry(root)

# Подключаем событие для изменения выпадающего списка
step_option.trace("w", toggle_boundary_field)

# Запуск главного цикла приложения
root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tk dropdown example")

# Добавляем сетку
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Создаём переменную Tkinter
tkvar = tk.StringVar(root)

# Список с вариантами
choices = ['Пицца', 'Лазанья', 'Фри', 'Рыба', 'Картофель']
tkvar.set('Пицца')  # задаём вариант по умолчанию

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
tk.Label(mainframe, text="Choose a dish").grid(row=1, column=0)
popupMenu.grid(row=2, column=0)

# При изменении значения выпадающего меню
def change_dropdown(*args):
    print(tkvar.get())

# Связываем функцию для изменения выпадающего меню
tkvar.trace('w', change_dropdown)

root.mainloop()"""

from tkinter import *
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x150") 
 
main_menu = Menu()
 
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
 
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")
 
root.config(menu=main_menu)
 
root.mainloop()