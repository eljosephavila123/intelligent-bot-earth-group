import json
import pymongo
from bson.json_util import dumps
import json
from pymongo import MongoClient
from bson.json_util import dumps
from dns import resolver
from datetime import date


client = MongoClient(
    "mongodb://admin:hgr4BvOeOME9R852@cluster0-shard-00-00.qmxmg.mongodb.net:27017,cluster0-shard-00-01.qmxmg.mongodb.net:27017,cluster0-shard-00-02.qmxmg.mongodb.net:27017/sophia?ssl=true&replicaSet=atlas-vb7337-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database("sophia")
collection = db.queries
"""
query = "Sea"
results = query_search(query)
insertDa = {"query": query, "results": results}
insertDB = collection.insert_one(insertDa)
"""
"""
file_keywords = open("search_engine/keywords.txt", "r")
for query in file_keywords:
    results = query_search(query.strip())
    insertDa = {"query": query.strip(), "results": results}
    insertDB = collection.insert_one(insertDa)
    print("----change----")

curson = collection.find({"query": "Earth observation"})
list_cur = list(curson)


json_data = dumps(list_cur, indent=2)

with open('data.json', 'w') as file:
    file.write(json_data)"""

# curson = collection.find({"query"})


def words_save():
    queries = [document['query'] for document in collection.find()]
    json_data_list = []
    for query in queries:
        json_data_list.append({"query": query})
    with open('./data/queries_title.json', 'w', encoding='utf-8') as f:
        json.dump(json_data_list, f, ensure_ascii=False, indent=4)


# words_save()
def search_database(query):
    curson = collection.find({"query": query})
    list_cur = list(curson)
    return list_cur[0]["results"]


def input_new_queries(query):
    collection = db.new_queries
    today = str(date.today())
    insertDa = {"date": today, "query": query}
    insertDB = collection.insert_one(insertDa)
    return "sucess insert data"
