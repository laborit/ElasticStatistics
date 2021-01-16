import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging
import datetime
from elasticsearch import Elasticsearch

def es_data():

    data_raw = []
    for mounth in range(12, 13):
        for day in range(1, 31):
            es_answer = es.indices.stats(index=es_index(mounth, day), metric="store,docs")
            try:
                data_raw.append([datetime.date(2020,mounth, day),
                                     es_answer['_all']['primaries']['store']['size_in_bytes'],
                                     es_answer['_all']['primaries']['docs']['count']])
            except:
                data_raw = data_raw.loc([datetime.date(2020,mounth, day),
                                     0,
                                     0], ignore_index=True)


    data=pd.DataFrame(data_raw, columns=['Date','size','count'])

    #data = pd.DataFrame(data_raw, columns=['Date','size','count']),ignore_index=True,index_col=['Date'])
    data=data.set_index('Date')
    print(data)
    return data


def es_index(mounth,day):
    es_index = "*2020"
    if len(str(mounth)) == 1:
        es_index +="0"
    es_index +=str(mounth)
    if len(str(day)) == 1:
        es_index += "0"
    es_index += str(day)+"*"
    return es_index

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    data = es_data()
    data.to_csv('out.csv')

    fig, ax = plt.subplots()
    ax.tick_params(axis='both',  # Применяем параметры к обеим осям
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
    #plt.axis([0,5,0,20])
    plt.title('My first plot')
    plt.xlabel('Counting')
    plt.ylabel('Square values')
    plt.grid(True)
    #ax.tick_params
   # plt.bar(data.index,data['count'])
    plt.bar(data.index,data['size'])

    plt.show()



