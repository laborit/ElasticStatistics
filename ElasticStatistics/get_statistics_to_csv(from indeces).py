import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging
import datetime
from elasticsearch import Elasticsearch

# Получает статистику по индексам из elasticsearch, сохраняет в csv

def es_data(indeces_list):
    data_raw = []

    for indeces in indeces_list:
        es_index = indeces + "*"
        es_answer = es.indices.stats(index=es_index, metric="store,docs")
        try:
            data_raw.append([indeces, es_answer['_all']['primaries']['store']['size_in_bytes'],
                                es_answer['_all']['primaries']['docs']['count']])
        except:
            data_raw.append([indeces,0,0],)


    data=pd.DataFrame(data_raw, columns=['indeces','size','count'])
    data=data.set_index('indeces')
    print(data)
    return data


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    return _es

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    indeces_list=open('indeces_name.txt',encoding='utf-8').read().splitlines()
    print(indeces_list)
    data = es_data(indeces_list)
    data.to_csv('statistics_on_indeces.csv',encoding='utf-8')





