# insert data into elasticsearch

from elasticsearch import Elasticsearch
es = Elasticsearch()

docs=[{"id": "1", "name": "HQ Melt Icepops"}, {"id": "2", "name": "Squash City"}, {"id": "3", "name": "HQ Melt Icepops"}, {"id": "4", "name": "Slotervaart"}, {"id": "5", "name": "de Volkskrant"}, {"id": "6", "name": "Maoz Vegetarian"}, {"id": "7", "name": "Baseball Amsterdam"}, {"id": "8", "name": "Holland Casino"}, {"id": "9", "name": "Bar de Brederode"}, {"id": "10", "name": "Mimagine HQ"}, {"id": "11", "name": "Albert Heijn"}, {"id": "12", "name": "Startupbootcamp"}, {"id": "13", "name": "Westerpark"}, {"id": "14", "name": "J's Punani"}, {"id": "15", "name": "Kings Of Code Hack Battle"}, {"id": "16", "name": "Ciclo Rijwielen"}, {"id": "17", "name": "De Witte Vlinder"}, {"id": "18", "name": "Het Kaufhaus"}, {"id": "19", "name": "De Wasserette"}, {"id": "20", "name": "Jeugdbescherming Regio Amsterdam"}, {"id": "21", "name": "Doka"}]
[{"id": "1", "name": "HQ Melt Icepops"}, {"id": "2", "name": "Squash City"}, {"id": "3", "name": "HQ Melt Icepops"}, {"id": "4", "name": "Slotervaart"}, {"id": "5", "name": "de Volkskrant"}, {"id": "6", "name": "Maoz Vegetarian"}, {"id": "7", "name": "Baseball Amsterdam"}, {"id": "8", "name": "Holland Casino"}, {"id": "9", "name": "Bar de Brederode"}, {"id": "10", "name": "Mimagine HQ"}, {"id": "11", "name": "Albert Heijn"}, {"id": "12", "name": "Startupbootcamp"}, {"id": "13", "name": "Westerpark"}, {"id": "14", "name": "J's Punani"}, {"id": "15", "name": "Kings Of Code Hack Battle"}, {"id": "16", "name": "Ciclo Rijwielen"}, {"id": "17", "name": "De Witte Vlinder"}, {"id": "18", "name": "Het Kaufhaus"}, {"id": "19", "name": "De Wasserette"}, {"id": "20", "name": "Jeugdbescherming Regio Amsterdam"}, {"id": "21", "name": "Doka"}]
print(type(docs))
for i in range(21):
    # PUT
    res = es.index(
        index="bm25_test", doc_type='table', id=i + 1, body=docs[i])
    # GET
    res = es.get(index="bm25_test", doc_type='table', id=i + 1)
    print(res['_source'])

