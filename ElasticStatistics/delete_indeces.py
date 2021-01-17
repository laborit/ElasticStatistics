import logging
from elasticsearch import Elasticsearch

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    # if _es.ping():
    #     print('Yay Connect')
    # else:
    #     print('Awww it could not connect!')
    return _es

if __name__ == '__main__':
    # start_date, end_date = datetime.date(2020,7, 1), datetime.date.today()
    # day_count = (end_date - start_date).days + 1
    logging.basicConfig(level=logging.ERROR)
    es=connect_elasticsearch()
    es.indices.delete(index='*202007*', ignore=[400, 404])

    # data.to_csv('out.csv')