# insert data into elasticsearch
import json

json_file = open('cleaned_ams_venues_data.json')
json_str = json_file.read()
json_data = json.loads(json_str)

data = []
for key in json_data:
   temp =json_data[key]
   temp.update({"id": key,})
   data.append(temp)

from elasticsearch import Elasticsearch
es = Elasticsearch()

for i in range(len(data)):
    # PUT
    res = es.index(
        index="bm25_test", doc_type='table', id=i + 1, body=data[i])
    # GET
    res = es.get(index="bm25_test", doc_type='table', id=i + 1)
    
print('####Indexing is done####')
