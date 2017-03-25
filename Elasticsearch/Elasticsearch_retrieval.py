import json
from elasticsearch import Elasticsearch
es = Elasticsearch()

qry = {"query": 
           {"query_string": 
                {"query": "Movies"}
           }
      }
res = es.search(index="bm25_test", doc_type="table", body=qry)
print("%d documents found" % res['hits']['total'])

data = []
print(len(res['hits']['hits']))
for doc in res['hits']['hits']:
    print("%s | %s" % (doc['_source']['id'], doc['_source']['name']))
    data.append(doc['_source'])

with open('ElasticSearch_Query_Response.json', 'w') as outfile:
        json.dump(data, outfile)

print('####Data retrieval is done####')

