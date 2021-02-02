import json
import pymongo
from bson.json_util import dumps
import json
from pymongo import MongoClient
from bson.json_util import dumps
from dns import resolver
from datetime import date


client = MongoClient(
    "mongodb://test:pusr2qZqfq1pJbR2@cluster0-shard-00-00.qmxmg.mongodb.net:27017,cluster0-shard-00-01.qmxmg.mongodb.net:27017,cluster0-shard-00-02.qmxmg.mongodb.net:27017/sophia?ssl=true&replicaSet=atlas-vb7337-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database("sophia")
collection = db.queries


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
