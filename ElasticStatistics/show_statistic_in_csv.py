import numpy as np
import matplotlib.pyplot as plt
#  Подключаем модуль управления тиками:
import matplotlib.ticker as ticker
import pandas as pd
import datetime



def test():
    start_date, end_date = datetime.date(2020, 10, 1), datetime.date(2020, 10, 31)

    # data_csv = pd.read_csv('out.csv')
    # data_csv = data_csv.set_index('Date')
    # data = data_csv[str(start_date):str(end_date)]

    data_csv = pd.read_csv('statistics_on_indeces.csv')
    data_csv = data_csv.set_index('indeces')
    data=data_csv

    fig = plt.figure()
    ax_1 = fig.add_subplot(111)
    plt.grid(axis = 'y')

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

    # ax_1.set_title('Размер индексов по дням')
    ax_1.set_title('Размер индексов')

    ax_1.set_xlabel('Дата')
    ax_1.set_ylabel('Объем данных, Гб')
    ax_1.bar(data.index, data['size'], width=0.6, edgecolor='black')

    ax_2 = ax_1.twinx()
    ax_2.set_ylabel('Количество документов, тыс.шт.')
    ax_2.bar(data.index, data['count']/1000,color='green', width=0.5, edgecolor='black',align='edge')

    ax_1.legend(['Объем данных,'], loc='upper left')
    ax_2.legend(['Количество документов'],loc='upper right')


    fig.set_figwidth(19)  # ширина Figure (основной формы)
    fig.set_figheight(10)

    plt.show()

test()