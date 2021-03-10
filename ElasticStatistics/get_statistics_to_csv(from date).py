import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging
import datetime
from elasticsearch import Elasticsearch

# Получает статистику по датам из elasticsearch, сохраняет в csv

def es_data(start_date,end_date):
    data_raw = []
    day_count = (end_date - start_date).days + 1
    for date in (start_date + datetime.timedelta(n) for n in range(day_count)):
        es_index = "*" + str(date).replace("-", "") + "*"
        es_answer = es.indices.stats(index=es_index, metric="store,docs")
        try:
            data_raw.append([date, es_answer['_all']['primaries']['store']['size_in_bytes'],
                                es_answer['_all']['primaries']['docs']['count']])
        except:
            data_raw = data_raw.append([date,0,0], ignore_index=True)


    data=pd.DataFrame(data_raw, columns=['Date','size','count'])
    data=data.set_index('Date')
    print(data)
    return data


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    return _es

if __name__ == '__main__':
    start_date, end_date = datetime.date(2020,7, 1), datetime.date.today()
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    data = es_data(start_date, end_date)
    data.to_csv('out.csv')





