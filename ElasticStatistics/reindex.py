from elasticsearch import Elasticsearch

def es_data():

    Mapping = es.indices.get_mapping(index='1cchangelog_документ_заявкапокупателя_20210105')



    # Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['_source']= {"enabled":"false"} - отключаем _source


    for field in Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties']:
        if field=='СсылкаНаОбъект' or field=='Компьютер' or field=='Пользователь' or field=='Период':
            Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties'][field][
                'index'] = "true"
        else:
            for field2 in Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties'][field]:
                if field2=='properties':
                    for field3 in Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties'][field]['properties']:
                        Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties'][field][field2][field3][
                            'index'] = "false"

                else:
                    Mapping['1cchangelog_документ_заявкапокупателя_20210105']['mappings']['properties'][field][
                        'index'] = "false"
                    break

    es.indices.create(index='1cchangelog_документ_заявкапокупателя_20210105_test2', body=Mapping['1cchangelog_документ_заявкапокупателя_20210105'])
    es.reindex({
        "source": {"index": "1cchangelog_документ_заявкапокупателя_20210105"},
        "dest": {"index": "1cchangelog_документ_заявкапокупателя_20210105_test2"}
    })

    return Mapping


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}])
    return _es

if __name__ == '__main__':
    es=connect_elasticsearch()
    data = es_data()
    print(data)






