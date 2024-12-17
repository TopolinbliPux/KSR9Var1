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
    "maxN":10000,
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

label_N = tk.Label(frame2, text="Максимальное количество шагов", font=("Times New Roman", 10), bg="white")
entry_N = tk.Entry(frame2, font=("Times New Roman", 10))
entry_N.insert(0, str(default_values["maxN"]))  
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
method_combobox.set("РК4")  # Значение по умолчанию

# Размещение элементов в 3-й и 4-й колонках
label_method.grid(row=8, column=0, sticky="w", padx=5, pady=5)  # Размещаем label в 3-й колонке
method_combobox.grid(row=8, column=1, sticky="w",padx=0, pady=5)  # Размещаем combobox в 4-й колонке
# ------------------------------------------------создание меню для выбора метода-------------------------------------------------

# ------------------------------------------------Численные методы-------------------------------------------------
def mainFunction(x,v,sigma,alpha):
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator=-0.6*np.sqrt(2*g)*sigma
    denominator=TG*np.pi*v**(3/2) if v>0 else 0
    U=numerator/denominator
    return U

def istResh(x, v0, sigma, alpha):
    U_0 = v0 ** (5 / 2)
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator = -1.5 * np.sqrt(2 * g) * sigma * x
    denominator = TG * np.pi
    U = ((numerator / denominator) + U_0) ** (2 / 5) if ((numerator / denominator) + U_0)>0 else 0
    return U

def bigAndHalfStepForRK3(x,v,h,sigma,alpha):
    X=x
    vector_v=[0,0,0,0,0,0]
    k1 = mainFunction(X,v,sigma,alpha)
    k2 = mainFunction(X + h / 3, v + h / 3 * k1, sigma, alpha)
    k3 = mainFunction(X + 2 * h / 3, v + 2 * h / 3 * k2, sigma, alpha)

    V = v + h * (k1 / 4 + 3 * k3 / 4) #получили значение V для большого шага
    vector_v[2]=V
    #первый половинный шаг
    x_1_2 = x 
    k1 = mainFunction(x_1_2, v, sigma, alpha)
    k2 = mainFunction(x_1_2 + h / 6, v + h / 6 * k1, sigma, alpha)
    k3 = mainFunction(x_1_2 + h / 3, v + h / 3 * k2, sigma, alpha)
    
    v_1_2 = v + h / 2 * (k1 / 4 + 3 * k3 / 4) #получили значение v_1_2 для первого половинного шага
    vector_v[3] = v_1_2

    #второй половинный шаг
    x_2_2 = x_1_2 + h / 2
    k1 = mainFunction(x_2_2, v_1_2, sigma, alpha)
    k2 = mainFunction(x_2_2 + h / 6, v_1_2 + h / 6 * k1, sigma, alpha)
    k3 = mainFunction(x_2_2 + h / 3, v_1_2 + h / 3 * k2, sigma, alpha)
    v_2_2 = v_1_2 + h / 2 * (k1 / 4 + 3 *k3 / 4) #получили значение v_2_2 для второго половинного шага
    vector_v[4] = v_2_2

    #контрольная величина S
    S = (abs(vector_v[2] - vector_v[4]) / 7)
    vector_v[5]=S
    return vector_v

def methodRK3WithLocalErrorControl(x,v,h,sigma,alpha,epsilon,c1,c2):
    vector_v=bigAndHalfStepForRK3(x,v,h,sigma,alpha) 
    S=vector_v[5]
    while (S>=epsilon or vector_v[4]<0 or vector_v[3]<0):
        #деление шага
        h=h/2
        c1=c1+1
        #пересчет точки
        vector_v=bigAndHalfStepForRK3(x,v,h,sigma,alpha)  
        S=vector_v[5]
    if ((epsilon/16 <=S) and (S<=epsilon)):
        #не меняем шаг, принимаем точку
        vector_v[1]=vector_v[2]
    if (S<epsilon/16):
        #удвоение шага
        h=2*h
        c2=c2+1
        #принимаем точку, удваивая шаг
        vector_v[1]=vector_v[2]
    result=[x,vector_v,h,c1,c2]
    return result

def bigAndHalfStepForRK4(x,v,h,sigma,alpha):
    X=x
    vector_v=[0,0,0,0,0,0]
    k1 = mainFunction(X,v,sigma,alpha)
    k2 = mainFunction(X + h / 2, v + h / 2 * k1, sigma, alpha)
    k3 = mainFunction(X + h / 2, v + h / 2 * k2, sigma, alpha)
    k4 = mainFunction(X+h,v+h*k3,sigma, alpha)

    V = v + h/6 * (k1+2*k2+2*k3+k4) #получили значение V для большого шага
    vector_v[2]=V
    #первый половинный шаг
    x_1_2 = x 
    k12 = mainFunction(x_1_2, v, sigma, alpha)
    k21 = mainFunction(x_1_2 + h / 4, v + h / 4 * k12, sigma, alpha)
    k31 = mainFunction(x_1_2 + h / 4, v + h / 4 * k21, sigma, alpha)
    k41 = mainFunction(x_1_2+h/2,v+h/2*k31,sigma, alpha)
    
    v_1_2 = v + h / 12 * (k12+2*k21+2*k31+k41) #получили значение v_1_2 для первого половинного шага
    vector_v[3] = v_1_2

    #второй половинный шаг
    x_2_2 = x_1_2 + h / 2
    k12 = mainFunction(x_2_2, v_1_2, sigma, alpha)
    k22 = mainFunction(x_2_2 + h / 4, v_1_2 + h / 4 * k12, sigma, alpha)
    k32 = mainFunction(x_2_2 + h / 4, v_1_2 + h / 4 * k22, sigma, alpha)
    k42 = mainFunction(x_2_2+h/2,v+h/2*k32,sigma, alpha)
    v_2_2 = v_1_2 + h / 2 * (k12+2*k22+2*k32+k42) #получили значение v_2_2 для второго половинного шага
    vector_v[4] = v_2_2

    #контрольная величина S
    S = (abs(vector_v[2] - vector_v[4]) / 15)
    vector_v[5]=S
    return vector_v

def methodRK4WithLocalErrorControl(x,v,h,sigma,alpha,epsilon,c1,c2):
    vector_v=bigAndHalfStepForRK4(x,v,h,sigma,alpha) 
    S=vector_v[5]
    while (S>=epsilon or vector_v[4]<0 or vector_v[3]<0):
        #деление шага
        h=h/2
        c1=c1+1
        #пересчет точки
        vector_v=bigAndHalfStepForRK4(x,v,h,sigma,alpha)  
        S=vector_v[5]
    if (((epsilon/32) <=S) and (S<=epsilon)):
        #не меняем шаг, принимаем точку
        vector_v[1]=vector_v[2]
    if (S<(epsilon/32)):
        #удвоение шага
        h=2*h
        c2=c2+1
        #принимаем точку, удваивая шаг
        vector_v[1]=vector_v[2]
    result=[x,vector_v,h,c1,c2]
    return result

# ------------------------------------------------Численные методы-------------------------------------------------
# ------------------------------------------------Заполнение второго фрейма-------------------------------------------------

def is_nan(value):
    """Функция для проверки на NaN."""
    return np.isnan(value)

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
        maxN = int(entry_N.get())
        controlExit = float(entry_controlExit.get())

        # Получаем выбранный метод из combobox
        selected_method = method_combobox.get()

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

        c1_values=[]  # Список для хранения всех значений c1-деление шага
        c2_values=[]  # Список для хранения всех значений c2-удвоение шага
        h_values=[]   # Список для хранения шага
        Ei_values = []  # Список для хранения всех значений Ei
        OLP_values=[]  # Список для хранения ОЛП
        i_values=[] # Список для хранения номера шага

        # Условие для maxN != 0 и controlExit != 0
        if maxN != 0 and controlExit != 0:
            for i in range(1, maxN + 1):
                # Выбираем метод в зависимости от combobox
                if selected_method == "РК3":
                    result = methodRK3WithLocalErrorControl(x, v, h, sigma, alpha, epsilon, c1, c2)
                elif selected_method == "РК4":
                    result = methodRK4WithLocalErrorControl(x, v, h, sigma, alpha, epsilon, c1, c2)
                x, vector_v, h, c1, c2 = result
                xi = x
                vi = vector_v[1]
                v2i = vector_v[4]
                hi = h
                OLP = abs(v2i - vi)
                ui = istResh(x, v0, sigma, alpha)
                Ei = abs(vi - ui)

                # Проверяем на NaN перед вставкой
                #if is_nan(xi) or is_nan(vi) or is_nan(v2i) or is_nan(hi) or is_nan(OLP) or is_nan(ui) or is_nan(Ei):
                    #continue  # Пропускаем этот шаг, если есть NaN

                # Вставляем новые строки в таблицу
                treeview.insert("", "end", values=(
                    f"{i:5}",
                    f"{xi:.16f}",
                    f"{vi:.16f}",
                    f"{v2i:.16f}",
                    f"{hi:.16f}",
                    f"{OLP:.16f}",
                    f"{c1:.0f}",
                    f"{c2:.0f}",
                    f"{ui:.16f}",
                    f"{Ei:.16f}"
                ))

                # Добавляем значения в соответствующие списки
                c1_values.append(c1)
                c2_values.append(c2)
                h_values.append(h)
                Ei_values.append(Ei)
                OLP_values.append(OLP)
                i_values.append(i)

                # Добавляем данные для графика
                xi_values.append(xi)
                vi_values.append(vi)
                ui_values.append(ui)

                # Обновляем переменные для следующего шага
                v = vector_v[1]
                vector_v = [u0, v, 0, 0, 0, 0]
                x = x + h

                # Проверка на выход по controlExit
                if vi <= controlExit:
                    break  # Выход из цикла, если vi стало меньше controlExit

        # Условие для maxN == 0 и controlExit != 0
        elif maxN == 0 and controlExit != 0:
            vi = 1000  # Начальное значение vi, которое явно больше controlExit
            i = 0  # Счетчик шагов
            while vi > controlExit:
                i += 1
                # Выбираем метод в зависимости от combobox
                if selected_method == "РК3":
                    result = methodRK3WithLocalErrorControl(x, v, h, sigma, alpha, epsilon, c1, c2)
                elif selected_method == "РК4":
                    result = methodRK4WithLocalErrorControl(x, v, h, sigma, alpha, epsilon, c1, c2)
                x, vector_v, h, c1, c2 = result
                xi = x
                vi = vector_v[1]
                v2i = vector_v[4]
                hi = h
                OLP = abs(v2i - vi)
                ui = istResh(x, v0, sigma, alpha)
                Ei = abs(vi - ui)

                # Проверяем на NaN перед вставкой
                if is_nan(xi) or is_nan(vi) or is_nan(v2i) or is_nan(hi) or is_nan(OLP) or is_nan(ui) or is_nan(Ei):
                    continue  # Пропускаем этот шаг, если есть NaN

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

                # Добавляем значения в соответствующие списки
                c1_values.append(c1)
                c2_values.append(c2)
                h_values.append(h)
                Ei_values.append(Ei)
                OLP_values.append(OLP)
                i_values.append(i)

                # Добавляем данные для графика
                xi_values.append(xi)
                vi_values.append(vi)
                ui_values.append(ui)

                # Обновляем переменные для следующего шага
                v = vector_v[1]
                vector_v = [u0, v, 0, 0, 0, 0]
                x = x + h
        #убираем из списка Ei начальное значение 0
        Ei_values=Ei_values[1:]

        # Находим индекс максимальной ОЛП и соответствующее значение i
        max_OLP_index = OLP_values.index(max(OLP_values))
        max_OLP_i = i_values[max_OLP_index]

        # Находим индекс максимальной Ei и соответствующее значение i
        max_Ei_index = Ei_values.index(max(Ei_values))+1
        max_Ei_i = i_values[max_Ei_index]

        # Сохраняем данные для построения графика
        plot_graph.xi_values = xi_values
        plot_graph.vi_values = vi_values
        plot_graph.ui_values = ui_values

        plot_graph2.xi_values = xi_values
        plot_graph2.vi_values = vi_values

        # Строим график
        plot_graph(xi_values, vi_values, ui_values)
        plot_graph2(xi_values, vi_values)

        # Обновляем метки 
        c1_max = max(c1_values)
        c2_max = max(c2_values)
        h_max = max(h_values)
        h_min = min(h_values)
        OLP_max = max(OLP_values)
        Ei_max=max(Ei_values)
        max_xi=max(xi_values)

        label_c1_value.config(text=f"{c1_max:.0f}")
        label_c2_value.config(text=f"{c2_max:.0f}")
        label_max_h_value.config(text=f"{h_max:.16f}")
        label_min_h_value.config(text=f"{h_min:.16f}")
        label_max_OLP_value.config(text=f"{OLP_max:.16f}")
        label_max_Ei_values.config(text=f"{Ei_max:.16f}")
        label_max_xi.config(text=f"{max_xi:.16f}")
        # Добавляем информацию о шаге с максимальной ОЛП и максимальной Ei
        label_max_OLP_i.config(text=f"{max_OLP_i:.0f}")
        label_max_Ei_i.config(text=f"{max_Ei_i:.0f}")

        return 1

    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что все поля заполнены корректно.")
        return None

# кнопка для запуска вычислений
button_calculate = tk.Button(frame2, text="Начать расчёт", font=("Times New Roman", 10), command=calculate)
button_calculate.grid(row=8, column=4, columnspan=1, pady=10)

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
treeview.grid(row=0, column=2, columnspan=9, rowspan=8, padx=5, pady=5)  # Помещаем таблицу в первые 5 колонок

# Размещение вертикальной полосы прокрутки
y_scrollbar.grid(row=0, column=12, rowspan=7, sticky="ns")  # Прокрутка в 8-й колонке
y_scrollbar.config(command=treeview.yview)

treeview.configure(yscrollcommand=y_scrollbar.set)

#Вывод справки о методе
task_text_9="""Число делений"""
label9 = tk.Label(frame2, text=task_text_9, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label9.grid(column=9, row=10)

task_text_10="""Число удвоений"""
label10 = tk.Label(frame2, text=task_text_10, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label10.grid(column=9, row=11)

task_text_11="""Максимальный шаг"""
label11 = tk.Label(frame2, text=task_text_11, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label11.grid(column=9, row=12)

task_text_12="""Минимальный шаг"""
label12 = tk.Label(frame2, text=task_text_12, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label12.grid(column=9, row=13)

#task_text_13="""Минимальная ОЛП"""
#label13 = tk.Label(frame2, text=task_text_13, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
#label13.grid(column=9, row=14)

task_text_14="""Максимальная ОЛП"""
label14 = tk.Label(frame2, text=task_text_14, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label14.grid(column=9, row=15)
task_text_15="""достигается на шаге i="""
label15 = tk.Label(frame2, text=task_text_15, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label15.grid(column=9, row=16)

task_text_16="""Максимальная Ei"""
label16 = tk.Label(frame2, text=task_text_16, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label16.grid(column=9, row=17)
task_text_17="""достигается на шаге i="""
label17 = tk.Label(frame2, text=task_text_17, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label17.grid(column=9, row=18)

task_text_19="""Итоговое время:"""
label19 = tk.Label(frame2, text=task_text_19, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label19.grid(column=9, row=19)

# Метки для вывода значений
label_c1_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_c1_value.grid(column=10, row=10)

label_c2_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_c2_value.grid(column=10, row=11)

label_max_h_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_h_value.grid(column=10, row=12)

label_min_h_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_min_h_value.grid(column=10, row=13)

#label_min_OLP_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
#label_min_OLP_value.grid(column=10, row=14)

label_max_OLP_value = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_OLP_value.grid(column=10, row=15)

label_max_OLP_i = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_OLP_i.grid(column=10, row=16)

label_max_Ei_values = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_Ei_values.grid(column=10, row=17)

label_max_Ei_i = tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_Ei_i.grid(column=10, row=18)

label_max_xi= tk.Label(frame2, text="0", justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label_max_xi.grid(column=10, row=19)

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
frame_graph.grid(row=9, column=0, columnspan=8, rowspan=9, padx=0, pady=0, sticky="nsew")

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
Нужна для построения графика истинного решения,
вычисления ui и Ei
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
label_image_4.place(x=10, y=320)

task_text_6="""
vector_v
это вектор содержит: 
u0- начальная точка, нужная для расчета истинного решения
v-текущая точка
V- большой шаг 
v1_2- первый половинный шаг
v2_2- второй половинный шаг
S- контрольная величина
Передается в функции для расчёта "большого" и "половинного" 
шагов, изменяя его
Непосредственно используется в функциях РК, изменяя его 
в соответствии с контролем локальной погрешности
"""
#текст 6
label6 = tk.Label(frame3, text=task_text_6, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label6.place(x=10, y=420)

#фото vector_v
image_path_5 = "vector_v.png"
image_5 = Image.open(image_path_5)
image_5 = image_5.resize((181, 39))
photo_5 = ImageTk.PhotoImage(image_5)

label_image_5 = tk.Label(frame3, image=photo_5)
label_image_5.place(x=180, y=430)

task_text_7="""
bigAndHalfStepForRK3(x, v, h, sigma, alpha)
В начале функции вектор vector_v зануляется,
затем функция делает "большой" и "половинные" шаги
методом Рунге-Кутта 3-го порядка.
Возвращает vector_v типа [0,0,V,v12,v22,S],
где S=|vector_v[4]-vector_v[2]|/(2^p-1), p=3-порядок метода
Аналогично для функции 
bigAndHalfStepForRK4(x, v, h, sigma, alpha)"""
#Текст 7
label7 = tk.Label(frame3, text=task_text_7, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label7.place(x=500, y=10)

task_text_8="""
функция 
methodRK3WithLocalErrorControl(x,v,h,sigma,alpha,epsilon,c1,c2)
работает по принципу: пока контроль локальной погрешности S 
не находится в нужных пределах, мы уменьшаем шаг, увеличивая с1, далее
в зависимости от величины S, мы либо не меняем шаг, принимая рассчитанную
точку, либо удваиваем шаг, увеличивая c2.
Для функции methodRK4WithLocalErrorControl(x,v,h,sigma,alpha,epsilon,c1,c2)
аналогичная логика, только изменяется расчет S и диапазоны, потому что меняется значение
p- порядка метода: было p=3, стало p=4
"""
#Текст 8
label8 = tk.Label(frame3, text=task_text_8, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label8.place(x=500, y=200)

#фото контроль локальной погрешности
image_path_7 = "controlLocPogr.png"
image_7 = Image.open(image_path_7)
image_7 = image_7.resize((749, 314))
photo_7 = ImageTk.PhotoImage(image_7)

#фото большой и половинные шаги
#размещено после фото лок погрешности, чтобы было выше
image_path_6 = "большойиполовинныйшаг.png"
image_6 = Image.open(image_path_6)
image_6 = image_6.resize((474, 268))
photo_6 = ImageTk.PhotoImage(image_6)

label_image_6 = tk.Label(frame3, image=photo_6)
label_image_6.place(x=950, y=10)

label_image_7 = tk.Label(frame3, image=photo_7)
label_image_7.place(x=500, y=400)

# ------------------------------------------------Оформление третьего фрейма-------------------------------------------------
# ------------------------------------------------Оформление четвертого фрейма-------------------------------------------------
frame4 = tk.Frame(notebook, bg="white")
frame4.pack(fill=BOTH, expand=True)
notebook.add(frame4, text="Наглядный функционал 2")
task_text_18="""
функция calculate()
Эта функция вызывается по нажатию кнопки "Начать расчёт",
очищает таблицу и графики, считывает введенные значения,
в первую строчку таблицы вводит начальные точки: x0,v0,u0 и нулевой шаг,
создает списки для хранения результатов, нужные для создания "справки" о решении,
Затем проверяются условия 
1) if (maxN != 0 and controlExit != 0) - хотим контролировать выход за нижнюю границу и, если вычисления слишком долгие, остановиться на максимальном шаге
2) elif (maxN == 0 and controlExit != 0)- хотим узнать точное время (xi), за которое вытечет вода

В каждом из них выбирается метод RK3 или RK4, которым будет производиться расчёт.
Перед вставкой полученных результатов есть проверка на NaN, чтобы подобные значения не выводились в таблицу.
Обновляются списки, графики, vector_v- обновляем точку, x.
Происходит проверка на выход за нижнюю границу.

В первом случае в цикле от 1 до maxN+1 проводится расчёт точек, в зависимости от выбранного метода, вычисления преращаются при условии if vi <= controlExit
Во втором случае сначала задается очень большая величина vi (vector_v[1]), чтобы запустить цикл while vi < contolExit.
vi сразу же меняется под действием функции RK3/RK4

Затем находятся и выполняются данные для справки
"""

#Текст 18
label18 = tk.Label(frame4, text=task_text_18, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label18.place(x=10, y=10)

# ------------------------------------------------Оформление четвертого фрейма-------------------------------------------------

# ------------------------------------------------Оформление пятого фрейма-------------------------------------------------
frame5 = tk.Frame(notebook, bg="white")
frame5.pack(fill=BOTH, expand=True)
notebook.add(frame5, text="Интерпретация решения")

#фото параметр sigma
image_path_8 = "sigma.png"
image_8 = Image.open(image_path_8)
image_8 = image_8.resize((803, 301))
photo_8 = ImageTk.PhotoImage(image_8)

label_image_8 = tk.Label(frame5, image=photo_8)
label_image_8.place(x=10, y=70)

#фото параметр alpha
image_path_9 = "alpha.png"
image_9 = Image.open(image_path_9)
image_9 = image_9.resize((801, 344))
photo_9 = ImageTk.PhotoImage(image_9)

label_image_9 = tk.Label(frame5, image=photo_9)
label_image_9.place(x=10, y=400)
# ------------------------------------------------Фформление пятого  фрейма-------------------------------------------------
# ------------------------------------------------Фформление шестого  фрейма-------------------------------------------------
frame6 = tk.Frame(notebook, bg="white")
frame6.pack(fill=BOTH, expand=True)
notebook.add(frame6, text="Сравнение с 3 вариантом")


# Значения по умолчанию для каждого параметра
default_values = {
    "sigma": 0.1,
    "alpha": 30,
    "R":3,
    "x0": 0,
    "v0": 2,
    "h": 0.01,
    "epsilon": 0.0001,
    "maxN":10000,
    "controlExit":0.001
}

label_sigma2 = tk.Label(frame6, text="sigma:", font=("Times New Roman", 10), bg="white")
entry_sigma2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_sigma2.insert(0, str(default_values["sigma"]))  
label_sigma2.grid(row=0, column=0, sticky="w", padx=5, pady=0)
entry_sigma2.grid(row=0, column=1, padx=5, pady=0)

label_alpha2 = tk.Label(frame6, text="alpha:", font=("Times New Roman", 10), bg="white")
entry_alpha2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_alpha2.insert(0, str(default_values["alpha"])) 
label_alpha2.grid(row=1, column=0, sticky="w", padx=5, pady=0)
entry_alpha2.grid(row=1, column=1, padx=5, pady=0)

label_R2 = tk.Label(frame6, text="R:", font=("Times New Roman", 10), bg="white")
entry_R2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_R2.insert(0, str(default_values["R"]))  
label_R2.grid(row=2, column=0, sticky="w", padx=5, pady=0)
entry_R2.grid(row=2, column=1, padx=5, pady=0)

label_x02 = tk.Label(frame6, text="x0:", font=("Times New Roman", 10), bg="white")
entry_x02 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_x02.insert(0, str(default_values["x0"])) 
label_x02.grid(row=3, column=0, sticky="w", padx=5, pady=0)
entry_x02.grid(row=3, column=1, padx=5, pady=0)

label_v02 = tk.Label(frame6, text="v0:", font=("Times New Roman", 10), bg="white")
entry_v02 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_v02.insert(0, str(default_values["v0"]))  
label_v02.grid(row=4, column=0, sticky="w", padx=5, pady=0)
entry_v02.grid(row=4, column=1, padx=5, pady=0)

label_h2 = tk.Label(frame6, text="h:", font=("Times New Roman", 10), bg="white")
entry_h2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_h2.insert(0, str(default_values["h"])) 
label_h2.grid(row=5, column=0, sticky="w", padx=5, pady=0)
entry_h2.grid(row=5, column=1, padx=5, pady=0)

label_epsilon2 = tk.Label(frame6, text="epsilon:", font=("Times New Roman", 10), bg="white")
entry_epsilon2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_epsilon2.insert(0, str(default_values["epsilon"]))  
label_epsilon2.grid(row=6, column=0, sticky="w", padx=5, pady=0)
entry_epsilon2.grid(row=6, column=1, padx=5, pady=0)

label_N2 = tk.Label(frame6, text="Максимальное количество шагов", font=("Times New Roman", 10), bg="white")
entry_N2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_N2.insert(0, str(default_values["maxN"]))  
label_N2.grid(row=7, column=0, sticky="w", padx=5, pady=0)
entry_N2.grid(row=7, column=1, padx=5, pady=0)

label_controlExit2 = tk.Label(frame6, text="Контроль выхода за правую границу", font=("Times New Roman", 10), bg="white")
entry_controlExit2 = tk.Entry(frame6, font=("Times New Roman", 10))
entry_controlExit2.insert(0, str(default_values["controlExit"]))  
label_controlExit2.grid(row=8, column=0, sticky="w", padx=5, pady=0)
entry_controlExit2.grid(row=8, column=1, padx=5, pady=0)


def mainFunction2(x2, v2, R2, sigma2):
    numerator = -0.6 * sigma2 * np.sqrt(2 * g)
    denominator = np.pi * v2**(1/2) * (2 * R2 - v2)
    U2 = numerator / denominator
    return U2

def bigAndHalfStepForRK42(x2, v2, h2, R2, sigma2):
    X2 = x2 + h2
    vector_v2 = [0, 0, 0, 0, 0, 0]
    k1 = mainFunction2(X2, v2, R2, sigma2)
    k2 = mainFunction2(X2 + h2 / 2, v2 + h2 / 2 * k1, R2, sigma2)
    k3 = mainFunction2(X2 + h2 / 2, v2 + h2 / 2 * k2, R2, sigma2)
    k4 = mainFunction2(X2 + h2, v2 + h2 * k3, R2, sigma2)

    V2 = v2 + h2 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)  # получаем значение V для большого шага
    vector_v2[2] = V2

    # первый половинный шаг
    x_1_2 = x2 + h2 / 2
    k12 = mainFunction2(x_1_2, v2, R2, sigma2)
    k21 = mainFunction2(x_1_2 + h2 / 4, v2 + h2 / 4 * k12, R2, sigma2)
    k31 = mainFunction2(x_1_2 + h2 / 4, v2 + h2 / 4 * k21, R2, sigma2)
    k41 = mainFunction2(x_1_2 + h2 / 2, v2 + h2 / 2 * k31, R2, sigma2)

    v_1_2 = v2 + h2 / 12 * (k12 + 2 * k21 + 2 * k31 + k41)  # получаем значение v_1_2 для первого половинного шага
    vector_v2[3] = v_1_2

    # второй половинный шаг
    x_2_2 = x_1_2 + h2 / 2
    k12 = mainFunction2(x_2_2, v_1_2, R2, sigma2)
    k22 = mainFunction2(x_2_2 + h2 / 4, v_1_2 + h2 / 4 * k12, R2, sigma2)
    k32 = mainFunction2(x_2_2 + h2 / 4, v_1_2 + h2 / 4 * k22, R2, sigma2)
    k42 = mainFunction2(x_2_2 + h2 / 2, v_1_2 + h2 / 2 * k32, R2, sigma2)

    v_2_2 = v_1_2 + h2 / 2 * (k12 + 2 * k22 + 2 * k32 + k42)  # получаем значение v_2_2 для второго половинного шага
    vector_v2[4] = v_2_2

    # контрольная величина S
    S2 = abs(vector_v2[2] - vector_v2[4]) / 15
    vector_v2[5] = S2
    return vector_v2

def methodRK4WithLocalErrorControl2(x2, v2, h2, R2, sigma2, epsilon2, c12, c22):
    vector_v2 = bigAndHalfStepForRK42(x2, v2, h2, R2, sigma2)
    S2 = vector_v2[5]
    while S2 >= epsilon2:
        # деление шага
        h2 = h2 / 2
        c12 = c12 + 1
        # пересчет точки
        vector_v2 = bigAndHalfStepForRK42(x2, v2, h2, R2, sigma2)
        S2 = vector_v2[5]
    if epsilon2 / 32 <= S2 <= epsilon2:
        # не меняем шаг, принимаем точку
        vector_v2[1] = vector_v2[2]
    if S2 < epsilon2 / 32:
        # удвоение шага
        h2 = 2 * h2
        c22 = c22 + 1
        # принимаем точку, удваивая шаг
        vector_v2[1] = vector_v2[2]
    result = [x2, vector_v2, h2, c12, c22]
    return result

def plot_graph2(xi_values2, vi_values2):

    # Создаем фигуру и оси для графика
    fig, ax = plt.subplots(figsize=(10, 5))

    # Строим график зависимости vi от xi с синими точками (численное решение)
    ax.plot(xi_values2, vi_values2, label="vi(xi) - численное решение", color="b", marker="o", markersize=2)

    # Настройки графика
    ax.set_title("График зависимости vi от xi", fontsize=14)
    ax.set_xlabel("xi", fontsize=12)
    ax.set_ylabel("vi ", fontsize=12)
    ax.grid(True)
    ax.legend()

    # Удалим предыдущий график, если он существует
    if hasattr(plot_graph2, "canvas"):
        plot_graph2.canvas.get_tk_widget().destroy()

    # Создаём новый canvas для нового графика
    plot_graph2.canvas = FigureCanvasTkAgg(fig, frame_graph2)
    plot_graph2.canvas.draw()

    # Обновляем расположение графика
    plot_graph2.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

# Размещение фрейма для графика с использованием grid
frame_graph2 = tk.Frame(frame6, bg="white")
frame_graph2.grid(row=9, column=1, columnspan=8, rowspan=9, padx=0, pady=0, sticky="nsew")

frame6.grid_rowconfigure(9, weight=1)  # Даем вес 1 для строки с графиком
frame6.grid_columnconfigure(0, weight=1)  # Даем вес 1 для первой колонки
frame6.grid_columnconfigure(1, weight=1)  # Даем вес 1 для второй колонки
frame6.grid_columnconfigure(2, weight=2)  # Даем вес 2 для колонок с таблицей (чтобы они были шире)
frame6.grid_columnconfigure(3, weight=2)  # для остальных колонок таблицы, если нужно
frame6.grid_columnconfigure(4, weight=2)  # и т.д. для нужных колонок

"""def plot_graph2(xi_values, vi_values):
    # Создаем фигуру и оси для графика
    fig, ax = plt.subplots(figsize=(10, 5))

    # Строим график зависимости vi от xi с синими точками (численное решение)
    ax.plot(xi_values, vi_values, label="vi(xi) - численное решение", color="b", marker="o", markersize=2)

    # Настройки графика
    ax.set_title("График зависимости vi от xi", fontsize=14)
    ax.set_xlabel("xi", fontsize=12)
    ax.set_ylabel("vi", fontsize=12)
    ax.grid(True)
    ax.legend()

    # Удалим предыдущий график, если он существует
    if hasattr(plot_graph2, "canvas"):
        plot_graph2.canvas.get_tk_widget().destroy()

    # Создаем новый canvas для нового графика
    plot_graph2.canvas = FigureCanvasTkAgg(fig, frame_graph2)
    plot_graph2.canvas.draw()

    # Обновляем расположение графика
    plot_graph2.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)"""

# Размещение фрейма для графика с использованием grid
#frame_graph2 = tk.Frame(frame6, bg="white")
#frame_graph2.grid(row=9, column=1, columnspan=8, rowspan=9, padx=0, pady=0, sticky="nsew")

# Настройка row и column для grid
frame6.grid_rowconfigure(9, weight=1)
frame6.grid_columnconfigure(1, weight=1)
xi_values2 = []
vi_values2 = []
def calculate2():
    try:
        calculate()
        c12 = c22 = 0
        #plt.clf()  # Очистить график
        xi_values2.clear()  # Очистить предыдущие значения
        vi_values2.clear()

        # Считываем новые значения из полей ввода
        sigma2 = float(entry_sigma2.get())
        alpha2 = float(entry_alpha2.get())
        R2 = float(entry_R2.get())
        x02 = float(entry_x02.get())
        v02 = float(entry_v02.get())
        h2 = float(entry_h2.get())
        epsilon2 = float(entry_epsilon2.get())
        maxN2 = int(entry_N2.get())
        controlExit2 = float(entry_controlExit2.get())

        # Начальные условия
        u02 = v02
        x2 = x02
        v2 = v02

        # Условие для maxN != 0 и controlExit != 0
        if maxN2 != 0 and controlExit2 != 0:
            for i in range(1, maxN2 + 1):
                result2 = methodRK4WithLocalErrorControl2(x2, v2, h2, R2, sigma2, epsilon2, c12, c22)
                x2, vector_v2, h2, c12, c22 = result2
                xi2 = x2
                vi2 = vector_v2[1]
                xi_values2.append(xi2)
                vi_values2.append(vi2)

                v2 = vector_v2[1]
                vector_v2 = [u02, v2, 0, 0, 0, 0]
                x2 = x2 + h2

                if vi2 <= controlExit2:
                    break

        # Условие для maxN == 0 и controlExit != 0
        elif maxN2 == 0 and controlExit2 != 0:
            vi2 = 1000
            while vi2 > controlExit2:
                result2 = methodRK4WithLocalErrorControl2(x2, v2, h2, R2, sigma2, epsilon2, c12, c22)
                x2, vector_v2, h2, c12, c22 = result2
                xi2 = x2
                vi2 = vector_v2[1]
                xi_values2.append(xi2)
                vi_values2.append(vi2)

                v2 = vector_v2[1]
                vector_v2 = [u02, v2, 0, 0, 0, 0]
                x2 = x2 + h2

        # Строим график
        plot_graph2(xi_values2, vi_values2)
        return 1

    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что все поля заполнены корректно.")
        return None

# Кнопка для запуска вычислений
button_calculate2 = tk.Button(frame6, text="Показать графики", font=("Times New Roman", 10), command=calculate2)
button_calculate2.grid(row=1, column=2, pady=10)

# Сохраняем данные для построения графика
plot_graph.xi_values2 = xi_values2
plot_graph.vi_values2 = vi_values2

fsdsfsd=[]
# Строим график
plot_graph(xi_values2, vi_values2,fsdsfsd)

task_text_20="""Сосуд представляет собой полусферическую
чашу радиуса R с отверстием для слива площадью sigma.
Истечение воды описывается ДУ:"""

#Текст 20
label20 = tk.Label(frame6, text=task_text_20, justify=tk.LEFT, font=("Times New Roman", 12), padx=5, pady=2, bg="white")
label20.place(x=10, y=250)

image_path_10 = "6frame.png"
image_10 = Image.open(image_path_10)
image_10 = image_10.resize((332, 247))
photo_10 = ImageTk.PhotoImage(image_10)

label_image_10 = tk.Label(frame6, image=photo_10)
label_image_10.place(x=10, y=400)

# ------------------------------------------------Фформление шестого  фрейма-------------------------------------------------

root.mainloop()
