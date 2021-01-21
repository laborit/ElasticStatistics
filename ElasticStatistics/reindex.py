from elasticsearch import Elasticsearch

def es_data():

    es_answer = es.indices.get_mapping(index='1cchangelog_документ_заявкапокупателя_20210105')


    Mapping=es_answer



    # Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties']['index'] = "false"
    Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties']['СсылкаНаОбъект']['index'] = "true"
    print(Mapping)

    # es_answer = es.indices.create('nest', body=Mapping['1cchangelog_документ_заявкапокупателя_20210105'])

    es_answer = es.indices.put_mapping(Mapping['1cchangelog_документ_заявкапокупателя_20210105'],index='1cchangelog_документ_заявкапокупателя_20210105')

    return es_answer


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    return _es

if __name__ == '__main__':
    es=connect_elasticsearch()
    data = es_data()
    print(data)
    # data.to_csv('out.csv')





