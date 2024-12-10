import tkinter as tk

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
