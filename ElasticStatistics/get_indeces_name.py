# import matplotlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
import logging
# import datetime
from elasticsearch import Elasticsearch

# Получает список индексов из elasticsearch сохраняет в indeces_name.txt

def es_data():
    indeces_list = []
    indeces_name=open('indeces_name.txt', 'w',encoding='utf-8')
    # day_count = (end_date - start_date).days + 1
    # for date in (start_date + datetime.timedelta(n) for n in range(day_count)):
    #     es_index = "*" + str(date).replace("-", "") + "*"
    es_answer = es.indices.stats()
        # try:
    data_raw=es_answer['indices']
    print(len(data_raw))
    for key, item in data_raw.items():
        key=key.strip()
        if len(key)>21:
            key=key[:-9]
        if indeces_list.count(key) ==0:
            indeces_list.append(key)


    # except:
    #     data_raw = data_raw.loc([date,0,0], ignore_index=True)


    # data=pd.DataFrame(data_raw, columns=['Date','size','count'])
    # data=data.set_index('Date')
    indeces_list.sort()
    for item in indeces_list:
        print(item)
        indeces_name.write(item)
        indeces_name.write('\n')
    indeces_name.close()

    return data_raw


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}], timeout=30)
    # if _es.ping():
    #     print('Yay Connect')
    # else:
    #     print('Awww it could not connect!')
    return _es

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    data = es_data()






