import logging
from elasticsearch import Elasticsearch

# удаляет индексы

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    return _es

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    es.indices.delete(index='*202102*', ignore=[400, 404])

