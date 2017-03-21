import json
from elasticsearch import Elasticsearch
es = Elasticsearch()


json_file = open('venues_data.json')
json_str = json_file.read()
json_data = json.loads(json_str)
#print(type(json_data[0]))
#print(type(json_data["4d6fc293b09a8eecdbc685fe"]["tips"]["items"]))
data = []
for i in range(len(json_data)):
    #print(json_data[i]["venue"]["id"])
    #data.append({"id": i+1, 'venue id': json_data[i]["venue"]["id"], 'year' : json_data[i]["venue"]["location"docs["city"]})
    data.append({"id": str(i+1),'name' : json_data[i]["venue"]["name"]})

print(json.dumps(data))
docs={}
docs = json.dumps(data)
print(type(docs))
'''
for i in range(21):
    # PUT
    res = es.index(
        index="bm25_test", doc_type='table', id=i + 1, body=docs[i])
    # GET
    res = es.get(index="bm25_test", doc_type='table', id=i + 1)
    print(res['_source'])

'''
