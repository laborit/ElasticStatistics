from elasticsearch import Elasticsearch
import datetime

def get_indices (month, indeces):
    index_name_list=[]
    es_answer = es.indices.stats(index=indeces+month+"*")

    for key, item in es_answer['indices'].items():
        key=key.strip()
        index_name_list.append(key)

    index_name_list.sort()
    from elasticsearch import Elasticsearch
    import time

    def get_indices(month, indeces):
        index_name_list = []
        es_answer = es.indices.stats(index=indeces + month + "*")

        for key, item in es_answer['indices'].items():
            key = key.strip()
            index_name_list.append(key)

        index_name_list.sort()

        return index_name_list

    def Mapping(last_index_name):
        Mapping = es.indices.get_mapping(index=last_index_name)[last_index_name]
        for field in Mapping['mappings']['properties']:
            if field == 'СсылкаНаОбъект' or field == 'Компьютер' or field == 'Пользователь' or field == 'Период':
                Mapping['mappings']['properties'][field]['index'] = "true"
            else:
                for field2 in Mapping['mappings']['properties'][field]:
                    if field2 == 'properties':
                        for field3 in \
                                Mapping['mappings']['properties'][field]['properties']:
                            Mapping['mappings']['properties'][field][field2][field3]['index'] = "false"
                    else:
                        Mapping['mappings']['properties'][field]['index'] = "false"
                        break
        # print(Mapping)
        return Mapping

    def create_index(create_index_name, last_index_name):
        if not es.indices.exists(index=create_index_name):
            es.indices.create(index=create_index_name, body=Mapping(last_index_name))
            time.sleep(3)

    def reindex(create_index_name, index_name_list):
        print(create_index_name, es.count(index=create_index_name)['count'])
        if es.count(index=create_index_name)['count'] == 0:
            es.reindex({
                "source": {"index": index_name_list},
                "dest": {"index": create_index_name}
            }, slices="auto")
            # requests_per_second = 100
            time.sleep(10)

    def connect_elasticsearch():
        _es = None
        _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}], timeout=3600)
        return _es

    if __name__ == '__main__':
        year, month = "2021", "02"
        data_postfics = "_" + year + month
        indeces_list = open('indeces_name.txt', encoding='utf-8').read().splitlines()
        es = connect_elasticsearch()
        # for indeces in indeces_list:
        #     index_name_list=get_indices (data_postfics, indeces)
        #     if len(index_name_list) > 0:
        #         create_index_name=indeces+"_"+year+"mo"+month
        #         create_index(create_index_name, index_name_list[-1])
        #         print(create_index_name, index_name_list)

        for indeces in indeces_list:
            index_name_list = get_indices(data_postfics, indeces)
            if len(index_name_list) > 0:
                create_index_name = indeces + "_" + year + "mo" + month
                reindex(create_index_name, index_name_list)
                print(create_index_name)
        print("ок")

    return index_name_list

def Mapping(last_index_name):
    Mapping = es.indices.get_mapping(index=last_index_name)[last_index_name]
    for field in Mapping['mappings']['properties']:
        if field == 'СсылкаНаОбъект' or field == 'Компьютер' or field == 'Пользователь' or field == 'Период':
            Mapping['mappings']['properties'][field]['index'] = "true"
        else:
            for field2 in Mapping['mappings']['properties'][field]:
                if field2 == 'properties':
                    for field3 in \
                    Mapping['mappings']['properties'][field]['properties']:
                        Mapping['mappings']['properties'][field][field2][field3]['index'] = "false"
                else:
                    Mapping['mappings']['properties'][field]['index'] = "false"
                    break
    #print(Mapping)
    return Mapping

def create_index(create_index_name,last_index_name):
    if not es.indices.exists(index=create_index_name):
        es.indices.create(index=create_index_name, body=Mapping(last_index_name))

def reindex(create_index_name, index_name_list):
    es.reindex({
        "source": {"index": index_name_list},
        "dest": {"index": create_index_name}
    }, wait_for_completion = "false")

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': '10.0.2.29', 'port': 9200}], timeout=30)
    return _es

if __name__ == '__main__':
    year, month="2020","08"
    data_postfics="_"+year+month
    indeces_list = open('indeces_name.txt', encoding='utf-8').read().splitlines()
    es=connect_elasticsearch()
    # for indeces in indeces_list:
    #     index_name_list=get_indices (data_postfics, indeces)
    #     if len(index_name_list) > 0:
    #         create_index_name=indeces+"_"+year+"mo"+month
    #         create_index(create_index_name, index_name_list[-1])
    #         print(create_index_name, index_name_list)

    for indeces in indeces_list:
        index_name_list = get_indices(data_postfics, indeces)
        if len(index_name_list)>0:
            create_index_name = indeces + "_" + year + "mo" + month
            reindex(create_index_name, index_name_list)
            print(create_index_name)
    print("ок")






