import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging
import datetime
from elasticsearch import Elasticsearch

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
            data_raw = data_raw.loc([date,0,0], ignore_index=True)


    data=pd.DataFrame(data_raw, columns=['Date','size','count'])
    data=data.set_index('Date')
    print(data)
    return data


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    # if _es.ping():
    #     print('Yay Connect')
    # else:
    #     print('Awww it could not connect!')
    return _es

if __name__ == '__main__':
    start_date, end_date = datetime.date(2020,7, 1), datetime.date.today()
    day_count = (end_date - start_date).days + 1
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    data = es_data(start_date, end_date)
    data.to_csv('out.csv')





