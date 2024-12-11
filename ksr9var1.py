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
# создаем фреймы
frame1 = tk.Frame(notebook, bg="white")
frame2 = tk.Frame(notebook, bg="white")
frame3 = tk.Frame(notebook, bg="white")
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
# Создаю 7 колоннок для второго фрейма
for i in range(8):
    frame2.grid_columnconfigure(i, weight=1)


# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Формулировка задачи")
notebook.add(frame2, text="Программная реализация")
notebook.add(frame3, text="Наглядный функционал")

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
label_image_2.place(x=10, y=395)
# ------------------------------------------------оформление первого фрейма-------------------------------------------------
# ------------------------------------------------оформление второго фрейма-------------------------------------------------
# Значения по умолчанию для каждого параметра
default_values = {
    "sigma": 0.1,
    "alpha": 30,
    "x0": 0,
    "v0": 2,
    "h": 0.01,
    "epsilon": 0.0001,
    "N":0,
    "controlExit":0.001
}

label_sigma = tk.Label(frame2, text="sigma:", font=("Times New Roman", 10), bg="white")
entry_sigma = tk.Entry(frame2, font=("Times New Roman", 10))
entry_sigma.insert(0, str(default_values["sigma"]))  
label_sigma.grid(row=0, column=0, sticky="w", padx=5, pady=0)
entry_sigma.grid(row=0, column=1, padx=5, pady=0)

label_alpha = tk.Label(frame2, text="alpha:", font=("Times New Roman", 10), bg="white")
entry_alpha = tk.Entry(frame2, font=("Times New Roman", 10))
entry_alpha.insert(0, str(default_values["alpha"])) 
label_alpha.grid(row=1, column=0, sticky="w", padx=5, pady=0)
entry_alpha.grid(row=1, column=1, padx=5, pady=0)

label_x0 = tk.Label(frame2, text="x0:", font=("Times New Roman", 10), bg="white")
entry_x0 = tk.Entry(frame2, font=("Times New Roman", 10))
entry_x0.insert(0, str(default_values["x0"])) 
label_x0.grid(row=2, column=0, sticky="w", padx=5, pady=0)
entry_x0.grid(row=2, column=1, padx=5, pady=0)

label_v0 = tk.Label(frame2, text="v0:", font=("Times New Roman", 10), bg="white")
entry_v0 = tk.Entry(frame2, font=("Times New Roman", 10))
entry_v0.insert(0, str(default_values["v0"]))  
label_v0.grid(row=3, column=0, sticky="w", padx=5, pady=0)
entry_v0.grid(row=3, column=1, padx=5, pady=0)

label_h = tk.Label(frame2, text="h:", font=("Times New Roman", 10), bg="white")
entry_h = tk.Entry(frame2, font=("Times New Roman", 10))
entry_h.insert(0, str(default_values["h"])) 
label_h.grid(row=4, column=0, sticky="w", padx=5, pady=0)
entry_h.grid(row=4, column=1, padx=5, pady=0)

label_epsilon = tk.Label(frame2, text="epsilon:", font=("Times New Roman", 10), bg="white")
entry_epsilon = tk.Entry(frame2, font=("Times New Roman", 10))
entry_epsilon.insert(0, str(default_values["epsilon"]))  
label_epsilon.grid(row=5, column=0, sticky="w", padx=5, pady=0)
entry_epsilon.grid(row=5, column=1, padx=5, pady=0)

label_N = tk.Label(frame2, text="Количество шагов", font=("Times New Roman", 10), bg="white")
entry_N = tk.Entry(frame2, font=("Times New Roman", 10))
entry_N.insert(0, str(default_values["N"]))  
label_N.grid(row=6, column=0, sticky="w", padx=5, pady=0)
entry_N.grid(row=6, column=1, padx=5, pady=0)

label_controlExit = tk.Label(frame2, text="Контроль выхода за правую границу", font=("Times New Roman", 10), bg="white")
entry_controlExit = tk.Entry(frame2, font=("Times New Roman", 10))
entry_controlExit.insert(0, str(default_values["controlExit"]))  
label_controlExit.grid(row=7, column=0, sticky="w", padx=5, pady=0)
entry_controlExit.grid(row=7, column=1, padx=5, pady=0)

# ------------------------------------------------создание меню для выбора метода-------------------------------------------------
# Создаем меню для выбора метода
label_method = tk.Label(frame2, text="Выберите метод:", font=("Times New Roman", 10), bg="white")
method_options = ["РК3", "РК4"]
method_combobox = ttk.Combobox(frame2, values=method_options, state="readonly", font=("Times New Roman", 10))
method_combobox.set("РК3")  # Значение по умолчанию

# Размещение элементов в 3-й и 4-й колонках
label_method.grid(row=8, column=0, sticky="w", padx=5, pady=5)  # Размещаем label в 3-й колонке
method_combobox.grid(row=8, column=1, sticky="w",padx=0, pady=5)  # Размещаем combobox в 4-й колонке
# ------------------------------------------------создание меню для выбора метода-------------------------------------------------

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
    k12 = mainFunction(x_2_2, v_1_2, sigma, alpha)
    k22 = mainFunction(x_2_2 + h / 6, v_1_2 + h / 6 * k12, sigma, alpha)
    k32 = mainFunction(x_2_2 + h / 3, v_1_2 + h / 3 * k22, sigma, alpha)
    v_2_2 = v_1_2 + h / 2 * (k12 / 4 + 3 *k22 / 4) #получили значение v_2_2 для второго половинного шага
    vector_v[4] = v_2_2

    #контрольная величина S
    S = abs(vector_v[2] - vector_v[4]) / 7
    vector_v[5]=S
    return vector_v

def methodRK3WithLocalErrorControl(x,v,h,N,sigma,alpha,epsilon,c1,c2):
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

def bigAndHalfStepForRK4(x,v,h,sigma,alpha):
    X=x+h
    vector_v=[0,0,0,0,0,0]
    k1 = mainFunction(X,v,sigma,alpha)
    k2 = mainFunction(X + h / 2, v + h / 2 * k1, sigma, alpha)
    k3 = mainFunction(X + h / 2, v + h / 2 * k2, sigma, alpha)
    k4 = mainFunction(X+h,v+h*k3)

    V = v + h/6 * (k1+2*k2+2*k3+k4) #получили значение V для большого шага
    vector_v[2]=V
    #первый половинный шаг
    x_1_2 = x + h / 2
    k12 = mainFunction(x_1_2, v, sigma, alpha)
    k21 = mainFunction(x_1_2 + h / 4, v + h / 4 * k1, sigma, alpha)
    k31 = mainFunction(x_1_2 + h / 4, v + h / 4 * k2, sigma, alpha)
    k41 = mainFunction(x_1_2+h/2,v+h/2*k3)
    
    v_1_2 = v + h / 12 * (k1+2*k2+2*k3+k4) #получили значение v_1_2 для первого половинного шага
    vector_v[3] = v_1_2

    #второй половинный шаг
    x_2_2 = x_1_2 + h / 2
    k12 = mainFunction(x_2_2, v_1_2, sigma, alpha)
    k22 = mainFunction(x_2_2 + h / 4, v_1_2 + h / 4 * k12, sigma, alpha)
    k32 = mainFunction(x_2_2 + h / 4, v_1_2 + h / 4 * k22, sigma, alpha)
    v_2_2 = v_1_2 + h / 2 * (k1+2*k2+2*k3+k4) #получили значение v_2_2 для второго половинного шага
    vector_v[4] = v_2_2

    #контрольная величина S
    S = abs(vector_v[2] - vector_v[4]) / 7
    vector_v[5]=S
    return vector_v

def methodRK4WithLocalErrorControl(x,v,h,N,sigma,alpha,epsilon,c1,c2):
    vector_v=bigAndHalfStepForRK4(x,v,h,sigma,alpha) 
    S=vector_v[5]
    while (S>=epsilon):
        #деление шага
        h=h/2
        c1=c1+1
        #пересчет точки
        vector_v=bigAndHalfStepForRK4(x,v,h,sigma,alpha)  
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
        # Очищаем таблицу
        for item in treeview.get_children():
            treeview.delete(item)

        plt.clf()  # Очистить график
        plot_graph.xi_values = []
        plot_graph.vi_values = []
        plot_graph.ui_values = []

        # Считываем новые значения из полей ввода
        sigma = float(entry_sigma.get())
        alpha = float(entry_alpha.get())
        x0 = float(entry_x0.get())
        v0 = float(entry_v0.get())
        h = float(entry_h.get())
        epsilon = float(entry_epsilon.get())
        N = int(entry_N.get())
        controlExit = float(entry_controlExit.get())

        c1 = 0   # счетчик числа деления шага
        c2 = 0   # счетчик числа удвоение шага

        # Начальные условия
        u0 = v0  # Начальное значение для u0

        # Добавляем начальную строку в таблицу
        treeview.insert("", "end", values=("0", x0, v0, "", "", "", "0", "0", u0, "0"))
        x = x0
        v = v0
        vector_v = [u0, v, 0, 0, 0, 0]  # Вектор для хранения значений
        xi_values = [x]
        vi_values = [v]
        ui_values = [istResh(x, u0, sigma, alpha)]  # Начальное значение ui

        # Условие для N != 0 (фиксированное количество шагов)
        if (N != 0 and controlExit == 0):
            for i in range(1, N + 1):
                result = methodRK3WithLocalErrorControl(x, v, h, N, sigma, alpha, epsilon, c1, c2)
                x, vector_v, h, c1, c2 = result
                xi = x
                vi = vector_v[1]
                v2i = vector_v[4]
                hi = h
                OLP = abs(v2i - vi)
                ui = istResh(x, v0, sigma, alpha)
                Ei = abs(vi - ui)

                # Вставляем новые строки в таблицу
                treeview.insert("", "end", values=(
                    f"{i:5}",
                    f"{xi:.5f}",
                    f"{vi:.16f}",
                    f"{v2i:.16f}",
                    f"{hi:.16f}",
                    f"{OLP:.16f}",
                    f"{c1:.0f}",
                    f"{c2:.0f}",
                    f"{ui:.16f}",
                    f"{Ei:.16f}"
                ))

                # Добавляем данные для графика
                xi_values.append(xi)
                vi_values.append(vi)
                ui_values.append(ui)

                # Обновляем переменные для следующего шага
                v = vector_v[1]
                vector_v = [u0, v, 0, 0, 0, 0]
                x = x + h

        # Условие для N == 0 (шаги до достижения controlExit)
        elif N == 0 and controlExit != 0:
            vi = 10000000  # Начальное значение vi, которое явно больше controlExit
            i = 0  # Счетчик шагов
            while vi > controlExit:
                i += 1
                result = methodRK3WithLocalErrorControl(x, v, h, 1, sigma, alpha, epsilon, c1, c2)
                x, vector_v, h, c1, c2 = result
                xi = x
                vi = vector_v[1]
                v2i = vector_v[4]
                hi = h
                OLP = abs(v2i - vi)
                ui = istResh(x, v0, sigma, alpha)
                Ei = abs(vi - ui)

                # Вставляем новые строки в таблицу
                treeview.insert("", "end", values=(
                    f"{i:5}",
                    f"{xi:.5f}",
                    f"{vi:.16f}",
                    f"{v2i:.16f}",
                    f"{hi:.16f}",
                    f"{OLP:.16f}",
                    f"{c1:.0f}",
                    f"{c2:.0f}",
                    f"{ui:.16f}",
                    f"{Ei:.16f}"
                ))

                # Добавляем данные для графика
                xi_values.append(xi)
                vi_values.append(vi)
                ui_values.append(ui)

                # Обновляем переменные для следующего шага
                v = vector_v[1]
                vector_v = [u0, v, 0, 0, 0, 0]
                x = x + h

        # Сохраняем данные для построения графика
        plot_graph.xi_values = xi_values
        plot_graph.vi_values = vi_values
        plot_graph.ui_values = ui_values

        # Строим график
        plot_graph(xi_values, vi_values, ui_values)

        return 1

    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что все поля заполнены корректно.")
        return None


# кнопка для запуска вычислений
button_calculate = tk.Button(frame2, text="Начать расчёт", font=("Times New Roman", 10), command=calculate)
button_calculate.grid(row=7, column=4, columnspan=1, pady=10)

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
treeview.grid(row=0, column=2, columnspan=6, rowspan=7, padx=5, pady=5)  # Помещаем таблицу в первые 5 колонок

# Размещение вертикальной полосы прокрутки
y_scrollbar.grid(row=0, column=8, rowspan=7, sticky="ns")  # Прокрутка в 8-й колонке
y_scrollbar.config(command=treeview.yview)

treeview.configure(yscrollcommand=y_scrollbar.set)

# ------------------------------------------------Построение графика-------------------------------------------------
def plot_graph(xi_values, vi_values, ui_values):

    # Создаем фигуру и оси для графика
    fig, ax = plt.subplots(figsize=(10, 5))

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
frame_graph.grid(row=9, column=0, columnspan=8, rowspan=4, padx=0, pady=0, sticky="nsew")

frame2.grid_rowconfigure(9, weight=1)  # Даем вес 1 для строки с графиком
frame2.grid_columnconfigure(0, weight=1)  # Даем вес 1 для первой колонки
frame2.grid_columnconfigure(1, weight=1)  # Даем вес 1 для второй колонки
frame2.grid_columnconfigure(2, weight=2)  # Даем вес 2 для колонок с таблицей (чтобы они были шире)
frame2.grid_columnconfigure(3, weight=2)  # для остальных колонок таблицы, если нужно
frame2.grid_columnconfigure(4, weight=2)  # и т.д. для нужных колонок


# ------------------------------------------------Построение графика-------------------------------------------------
# ------------------------------------------------оформление третьего фрейма-------------------------------------------------
task_text_4="""
mainFunction(x, v, sigma, alpha)
эта функция описывает дифференциальное уравнение
она нужна для расчёта коэффициентов в методе Рунге-Кутта 
при "большом" шаге и "половинными" шагами
"""
#текст 4
label4 = tk.Label(frame3, text=task_text_4, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label4.place(x=10, y=10)

#фото исходного ду
label_image_1 = tk.Label(frame3, image=photo_1)
label_image_1.place(x=10, y=115)

task_text_5="""
istResh(x, v0, sigma, alpha)
эта функция описывает истинное решение исходного ДУ
"""
#текст 5
label5 = tk.Label(frame3, text=task_text_5, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label5.place(x=10, y=215)

#фото общего решения
image_path_4 = "общее решение3.png"
image_4 = Image.open(image_path_4)
image_4 = image_4.resize((285, 96))
photo_4 = ImageTk.PhotoImage(image_4)

label_image_4 = tk.Label(frame3, image=photo_4)
label_image_4.place(x=10, y=300)

task_text_6="""
vector_v
это вектор содержит: 
u0- начальная точка, нужная для расчета истинного решения
v-текущая точка
V- большой шаг 
v1_2- первый половинный шаг
v2_2- второй половинный шаг
S- контрольная величина
"""
#текст 6
label6 = tk.Label(frame3, text=task_text_6, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label6.place(x=10, y=400)

#фото vector_v
image_path_5 = "vector_v.png"
image_5 = Image.open(image_path_5)
image_5 = image_5.resize((181, 39))
photo_5 = ImageTk.PhotoImage(image_5)

label_image_5 = tk.Label(frame3, image=photo_5)
label_image_5.place(x=180, y=410)

task_text_7="""
bigAndHalfStepForRK3(x, v, h, sigma, alpha)
В начале функции вектор vector_v зануляется,
затем функция делает"большой" и "половинные" шаги
методом Рунге-Кутта 3-го порядка.
Возвращает vector_v типа [0,0,V,v12,v22,S],
где S=|vector_v[4]-vector_v[2]|/(2^p-1), p=3-порядок метода"""
#Текст 7
label7 = tk.Label(frame3, text=task_text_7, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label7.place(x=500, y=10)

#фото большой и половинные шаги
image_path_6 = "большойиполовинныйшаг.png"
image_6 = Image.open(image_path_6)
image_6 = image_6.resize((474, 268))
photo_6 = ImageTk.PhotoImage(image_6)

label_image_6 = tk.Label(frame3, image=photo_6)
label_image_6.place(x=950, y=10)

# ------------------------------------------------оформление третьего фрейма-------------------------------------------------

root.mainloop()


