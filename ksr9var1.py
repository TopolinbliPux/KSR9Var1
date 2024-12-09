import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

g = 9.8

root = Tk()  # создание окна
root.title("Задача 9. Вариант 1. Вершинина ПМоП2")
root.iconbitmap(default="лиса.ico")  # добавление иконки)))
root.geometry("1920x1080")  # задание размера окна
# ------------------------------------------------оформление первого фрейма-------------------------------------------------
# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
# создаем пару фреймов
frame1 = tk.Frame(notebook, bg="white")
frame2 = tk.Frame(notebook, bg="white")
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Формулировка задачи")
notebook.add(frame2, text="Программная реализация")

task_text_1 = """
Сосуд для жидкости представляет собой коническую воронку (усеченный конус, коставленный на малый круг в основании)
с углом раствора alpha и отверстием для слива площадью sigma, расположенным на дне воронки. 
Истечение воды из отверстия в дне сосуда описывается дифференциальным уравнением: """

image_path_1 = "исходное ду.png"
image_1 = Image.open(image_path_1)
image_1 = image_1.resize((260, 102))
photo_1 = ImageTk.PhotoImage(image_1)

image_path_3 = "схемка.png"
image_3 = Image.open(image_path_3)
image_3 = image_3.resize((350, 217))
photo_3 = ImageTk.PhotoImage(image_3)

task_text_2 = """
Здесь u_0- высота свободной поверности жидкости над отверстием в начальный момент времени x_0=0;
u(x)- высота свободной поверхности жидкости над отверстием в момент времени x;
g- ускорение свободного падения
Параметры системы: alpha, sigma"""

task_text_3 = """
Получаем общее решение:
"""
image_path_2 = "общее решение2.png"
image_2 = Image.open(image_path_2)
image_2 = image_2.resize((491, 139))
photo_2 = ImageTk.PhotoImage(image_2)

#текст 1
label1 = tk.Label(frame1, text=task_text_1, justify=tk.LEFT, font=("Times New Roman", 12), padx=20, pady=5, bg="white")
label1.place(x=10, y=10)

#фото исходного ду
label_image_1 = tk.Label(frame1, image=photo_1)
label_image_1.place(x=10, y=115)

#фото схемки
label_image_3 = tk.Label(frame1, image=photo_3)
label_image_3.place(x=1000, y=50)

#текст 2
label2 = tk.Label(frame1, text=task_text_2, justify=tk.LEFT, font=("Times New Roman", 12), padx=20, pady=5, bg="white")
label2.place(x=10, y=215)

#текст 3
label3 = tk.Label(frame1, text=task_text_3, justify=tk.LEFT, font=("Times New Roman", 12), padx=20, pady=5, bg="white")
label3.place(x=10, y=320)

#фото общего решения
label_image_2 = tk.Label(frame1, image=photo_2)
label_image_2.place(x=10, y=395)  # Позиционируем второе изображение ниже текста
# ------------------------------------------------оформление первого фрейма-------------------------------------------------
# ------------------------------------------------оформление второго фрейма-------------------------------------------------
# Значения по умолчанию для каждого параметра
default_values = {
    "sigma": 0.1,
    "alpha": 30,
    "x0": 0,
    "v0": 2,
    "h": 0.01,
    "epsilon": 0.0001
}

label_sigma = tk.Label(frame2, text="sigma:", font=("Times New Roman", 10), bg="white")
entry_sigma = tk.Entry(frame2, font=("Times New Roman", 10))
entry_sigma.insert(0, str(default_values["sigma"]))  
label_sigma.grid(row=0, column=0, sticky="w", padx=5, pady=2)
entry_sigma.grid(row=0, column=1, padx=5, pady=2)

label_alpha = tk.Label(frame2, text="alpha:", font=("Times New Roman", 10), bg="white")
entry_alpha = tk.Entry(frame2, font=("Times New Roman", 10))
entry_alpha.insert(0, str(default_values["alpha"])) 
label_alpha.grid(row=1, column=0, sticky="w", padx=5, pady=2)
entry_alpha.grid(row=1, column=1, padx=5, pady=2)

label_x0 = tk.Label(frame2, text="x0:", font=("Times New Roman", 10), bg="white")
entry_x0 = tk.Entry(frame2, font=("Times New Roman", 10))
entry_x0.insert(0, str(default_values["x0"])) 
label_x0.grid(row=2, column=0, sticky="w", padx=5, pady=2)
entry_x0.grid(row=2, column=1, padx=5, pady=2)

label_v0 = tk.Label(frame2, text="v0:", font=("Times New Roman", 10), bg="white")
entry_v0 = tk.Entry(frame2, font=("Times New Roman", 10))
entry_v0.insert(0, str(default_values["v0"]))  
label_v0.grid(row=3, column=0, sticky="w", padx=5, pady=2)
entry_v0.grid(row=3, column=1, padx=5, pady=2)

label_h = tk.Label(frame2, text="h:", font=("Times New Roman", 10), bg="white")
entry_h = tk.Entry(frame2, font=("Times New Roman", 10))
entry_h.insert(0, str(default_values["h"])) 
label_h.grid(row=4, column=0, sticky="w", padx=5, pady=2)
entry_h.grid(row=4, column=1, padx=5, pady=2)

label_epsilon = tk.Label(frame2, text="epsilon:", font=("Times New Roman", 10), bg="white")
entry_epsilon = tk.Entry(frame2, font=("Times New Roman", 10))
entry_epsilon.insert(0, str(default_values["epsilon"]))  
label_epsilon.grid(row=5, column=0, sticky="w", padx=5, pady=2)
entry_epsilon.grid(row=5, column=1, padx=5, pady=2)
# ------------------------------------------------оформление второго фрейма-------------------------------------------------
# ------------------------------------------------Численные методы-------------------------------------------------
def mainFunction(x,v,sigma,alpha):
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator=-0.6*np.sqrt(2*g)*sigma
    denominator=TG*np.pi*v**(3/2)
    U=numerator/denominator
    return U

def istResh(x, v0, sigma, alpha):
    U_0 = v0 ** (5 / 2)
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator = -1.5 * np.sqrt(2 * g) * sigma * x
    denominator = TG * np.pi
    U = ((numerator / denominator) + U_0) ** (2 / 5)
    return U

def bigAndHalfStepForRK3(x,v,h,sigma,alpha):
    X=x+h
    vector_v=[0,0,0,0,0,0]
    k1 = mainFunction(X,v,sigma,alpha)
    k2 = mainFunction(X + h / 3, v + h / 3 * k1, sigma, alpha)
    k3 = mainFunction(X + 2 * h / 3, v + 2 * h / 3 * k2, sigma, alpha)

    V = v + h * (k1 / 4 + 3 * k3 / 4) #получили значение V для большого шага
    vector_v[2]=V
    #первый половинный шаг
    x_1_2 = x + h / 2
    k12 = mainFunction(x_1_2, v, sigma, alpha)
    k22 = mainFunction(x_1_2 + h / 6, v + h / 6 * k12, sigma, alpha)
    k32 = mainFunction(x_1_2 + h / 3, v + h / 3 * k22, sigma, alpha)
    
    v_1_2 = v + h / 2 * (k12 / 4 + 3 * k22 / 4) #получили значение v_1_2 для первого половинного шага
    vector_v[3] = v_1_2

	#второй половинный шаг
    x_2_2 = x_1_2 + h / 2
    k12 = mainFunction(x_2_2, v, sigma, alpha)
    k22 = mainFunction(x_2_2 + h / 6, v + h / 6 * k12, sigma, alpha)
    k32 = mainFunction(x_2_2 + h / 3, v + h / 3 * k22, sigma, alpha)
    v_2_2 = v_1_2 + h / 2 * (k12 / 4 + 3 *k22 / 4) #получили значение v_2_2 для второго половинного шага
    vector_v[4] = v_2_2

    #контрольная величина S
    S = abs(vector_v[2] - vector_v[4]) / 7
    vector_v[5]=S
    return vector_v

def methodRK3WithLocalErrorControl(x,v,h,N,sigma,alpha,epsilon):
    c1=0   #счетчик числа деления шага
    c2=0   #счетчик числа удвоение шага
    vector_v=bigAndHalfStepForRK3(x,v,h,sigma,alpha) 
    S=vector_v[5]
    while (S>=epsilon):
        #деление шага
        h=h/2
        c1=c1+1
        #пересчет точки
        vector_v=bigAndHalfStepForRK3(x,v,h,sigma,alpha)  
        S=vector_v[5]
    if ((epsilon/9 <=S) and (S<=epsilon)):
        #не меняем шаг, принимаем точку
        vector_v[1]=vector_v[2]
    if (S<epsilon/9):
        #удвоение шага
        h=2*h
        c2=c2+1
        #принимаем точку, удваивая шаг
        vector_v[1]=vector_v[2]
    result=[x,vector_v,h,c1,c2]
    return result
# ------------------------------------------------Численные методы-------------------------------------------------
# ------------------------------------------------Заполнение второго фрейма-------------------------------------------------
def calculate():
    try:
        # Получаем значения из полей ввода
        sigma = float(entry_sigma.get())
        alpha = float(entry_alpha.get())
        x0 = float(entry_x0.get())
        v0 = float(entry_v0.get())
        h = float(entry_h.get())
        epsilon = float(entry_epsilon.get())

        start_vector = [sigma, alpha, x0, v0, h, epsilon]
        u0 = v0  # Начальное значение для ui
        treeview.insert("", "end", values=("0", x0, v0, "", "", "", "0", "0", u0, "0"))
        N = 100
        x = x0
        v = v0
        vector_v = [u0, v, 0, 0, 0, 0]#создали вектор для хранения u0- начальная точка, нужная для расчета вспомогательной задачи Коши,v-текущая точка, V- большой шаг, v1_2- первый половинный шаг,v2_2- второй половинный шаг, S- контрольная величина

        # Списки для хранения значений xi, vi, ui (анализируем и сохраняем аналитическое решение)
        xi_values = [x]
        vi_values = [v]
        ui_values = [istResh(x, u0, sigma, alpha)]  # Сохраняем начальное значение ui

        for i in range(1, N + 1):
            result = methodRK3WithLocalErrorControl(x,v,h,N,sigma,alpha,epsilon)
            x, vector_v, h, c1, c2 = result
            xi = x
            vi = vector_v[1]
            v2i = vector_v[4]
            hi = h
            OLP = abs(v2i - vi)
            c1_val = c1
            c2_val = c2
            ui = istResh(x, v0, sigma, alpha)  # Аналитическое решение
            Ei = abs(vi - ui)
             # Форматируем значения с точностью до 5 знаков после запятой
            treeview.insert("", "end", values=(
                f"{i:5}",  # Столбец i, 5 знаков
                f"{xi:.5f}",  # Столбец xi, 5 знаков после запятой
                f"{vi:.16f}",  # Столбец vi, 5 знаков после запятой
                f"{v2i:.15f}",  # Столбец v2i, 5 знаков после запятой
                f"{hi:.5f}",  # Столбец hi, 5 знаков после запятой
                f"{OLP:.16f}",  # Столбец OLP, 5 знаков после запятой
                f"{c1_val:.0f}",  # Столбец c1, 5 знаков после запятой
                f"{c2_val:.0f}",  # Столбец c2, 5 знаков после запятой
                f"{ui:.16f}",  # Столбец ui, 5 знаков после запятой
                f"{Ei:.16f}"   # Столбец Ei, 5 знаков после запятой
            ))

            # Добавляем значения в списки для графика
            xi_values.append(xi)
            vi_values.append(vi)
            ui_values.append(ui)

            v=vector_v[1]
            vector_v = [u0, v, 0, 0, 0, 0]
            x = x + h  # Обновляем x

        # Сохраняем данные для построения графика
        plot_graph.xi_values = xi_values
        plot_graph.vi_values = vi_values
        plot_graph.ui_values = ui_values

        plot_graph(xi_values, vi_values, ui_values)
        return 1

    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что все поля заполнены корректно.")
        return None

# кнопка для запуска вычислений
button_calculate = tk.Button(frame2, text="Начать расчёт", font=("Times New Roman", 10), command=calculate)
button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

# Создаем вертикальную полосу прокрутки
y_scrollbar = tk.Scrollbar(frame2, orient="vertical")

# Создаем таблицу Treeview
treeview = ttk.Treeview(frame2, columns=("i", "xi", "vi", "v2i", "hi", "ОЛП", "c1", "c2", "ui", "Ei"), show="headings", yscrollcommand=y_scrollbar.set)

# Настройка заголовков
treeview.heading("i", text="i")
treeview.heading("xi", text="xi")
treeview.heading("vi", text="vi")
treeview.heading("v2i", text="v2i")
treeview.heading("hi", text="hi")
treeview.heading("ОЛП", text="ОЛП = |v2i - vi|")
treeview.heading("c1", text="c1")
treeview.heading("c2", text="c2")
treeview.heading("ui", text="ui")
treeview.heading("Ei", text="Ei")

# Определяем ширину столбцов
treeview.column("i", width=50)
treeview.column("xi", width=100)
treeview.column("vi", width=150)
treeview.column("v2i", width=150)
treeview.column("hi", width=100)
treeview.column("ОЛП", width=150)
treeview.column("c1", width=20)
treeview.column("c2", width=20)
treeview.column("ui", width=150)
treeview.column("Ei", width=150)

# Размещение таблицы справа от полей ввода
treeview.grid(row=0, column=2, rowspan=7, padx=20, pady=10)

# Размещение вертикальной полосы прокрутки
y_scrollbar.grid(row=0, column=3, rowspan=7, sticky="ns")
y_scrollbar.config(command=treeview.yview)

# ------------------------------------------------Построение графика-------------------------------------------------
def plot_graph(xi_values, vi_values, ui_values):

    # Создаем фигуру и оси для графика
    fig, ax = plt.subplots(figsize=(10, 6))

    # Строим график зависимости vi от xi с синими точками (численное решение)
    ax.plot(xi_values, vi_values, label="vi(xi) - численное решение", color="b", marker="o", markersize=2)

    # Строим красную траекторию зависимости ui от xi (аналитическое решение)
    ax.plot(xi_values, ui_values, label="ui(xi) - аналитическое решение", color="r", linestyle='-', linewidth=2)

    # Настройки графика
    ax.set_title("График зависимости vi и ui от xi", fontsize=14)
    ax.set_xlabel("xi", fontsize=12)
    ax.set_ylabel("vi / ui", fontsize=12)
    ax.grid(True)
    ax.legend()

    # Удалим предыдущий график, если он существует
    if hasattr(plot_graph, "canvas"):
        plot_graph.canvas.get_tk_widget().destroy()

    # Создаём новый canvas для нового графика
    plot_graph.canvas = FigureCanvasTkAgg(fig, frame_graph)
    plot_graph.canvas.draw()

    # Обновляем расположение графика
    plot_graph.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

# Размещение фрейма для графика с использованием grid
frame_graph = tk.Frame(frame2, bg="white")
frame_graph.grid(row=8, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

# Кнопка для построения графика
button_plot = tk.Button(frame2, text="Построить график", font=("Times New Roman", 10), command=plot_graph)
button_plot.grid(row=7, column=2, columnspan=2, pady=10)

# Убедитесь, что окна с графиком также растягиваются
frame2.grid_rowconfigure(8, weight=1)  # Разрешаем строке с графиком растягиваться
frame2.grid_columnconfigure(0, weight=1)  # Разрешаем первой колонке растягиваться
frame2.grid_columnconfigure(1, weight=1)  # Разрешаем второй колонке растягиваться
frame2.grid_columnconfigure(2, weight=1)  # Разрешаем третьей колонке растягиваться
frame2.grid_columnconfigure(3, weight=1)  # Разрешаем четвертой колонке растягиваться
# ------------------------------------------------Построение графика-------------------------------------------------

root.mainloop()
