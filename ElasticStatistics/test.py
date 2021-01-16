import numpy as np
import matplotlib.pyplot as plt
#  Подключаем модуль управления тиками:
import matplotlib.ticker as ticker
import pandas as pd



def test():
    data = pd.read_csv('out.csv')
    data = data.set_index('Date')

    fig = plt.figure()
    ax_1 = fig.add_subplot(2, 1, 1)
    ax_2 = fig.add_subplot(2, 1, 2)

    ax_1.tick_params(axis='x',  # Применяем параметры к обеим осям
                   which='major',  # Применяем параметры к основным делениям
                   # direction='inout',  # Рисуем деления внутри и снаружи графика
                   # length=20,  # Длинна делений
                   # width=4,  # Ширина делений
                   # color='m',  # Цвет делений
                   # pad=10,  # Расстояние между черточкой и ее подписью
                   labelsize=8,  # Размер подписи
                   # labelcolor='r',  # Цвет подписи
                   # bottom=True,  # Рисуем метки снизу
                   # top=True,  # сверху
                   # left=True,  # слева
                   # right=True,  # и справа
                   # labelbottom=True,  # Рисуем подписи снизу
                   # labeltop=True,  # сверху
                   # labelleft=True,  # слева
                   # labelright=True,  # и справа
                   labelrotation=90)  # Поворот подписей
    # plt.axis([0,5,0,20])
    ax_1.set_title('Размер индексов по дням')
    # ax_1.xlabel('Дата')
    # ax_1.ylabel('Объем данных, Гб')
    # ax_1.grid(which='major',axis='y')
    # plt.bar(data.index,data['count'])
    ax_1.bar(data.index, data['size'])



    ax_2.tick_params(axis='x',  # Применяем параметры к обеим осям
                   which='major',  # Применяем параметры к основным делениям
                   # direction='inout',  # Рисуем деления внутри и снаружи графика
                   # length=20,  # Длинна делений
                   # width=4,  # Ширина делений
                   # color='m',  # Цвет делений
                   # pad=10,  # Расстояние между черточкой и ее подписью
                   labelsize=8,  # Размер подписи
                   # labelcolor='r',  # Цвет подписи
                   # bottom=True,  # Рисуем метки снизу
                   # top=True,  # сверху
                   # left=True,  # слева
                   # right=True,  # и справа
                   # labelbottom=True,  # Рисуем подписи снизу
                   # labeltop=True,  # сверху
                   # labelleft=True,  # слева
                   # labelright=True,  # и справа
                   labelrotation=90)  # Поворот подписей
    # plt.axis([0,5,0,20])
    ax_2.set_title('Размер индексов по дням')
    # ax2.xlabel('Дата')
    # ax2.ylabel('Объем данных, Гб')
    # ax2.grid(which='major', axis='y')
    ax_2.bar(data.index,data['count'])
    #plt.bar(data.index, data['size'])

    fig.set_figwidth(20)  # ширина Figure
    fig.set_figheight(10)


    plt.show()

test()