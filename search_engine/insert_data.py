from scrapper.search_engines import Ask
from scrapper.search_engines.multiple_search_engines import MultipleSearchEngines, AllSearchEngines
import json
import pymongo
from bson.json_util import dumps
import json
from pymongo import MongoClient
from bson.json_util import dumps
from dns import resolver
from datetime import date
from htmldate import find_date

client = MongoClient(port=27017)
db = client.get_database("sophia")
collection = db.queries

def read_conteiners():
    file_contents = open('search_engine/data.txt', 'r')
    return [linea.rstrip() for linea in file_contents]

def query_search(query):
    dict_results = {
        "programs": [], "seminar": [], "symposium": [], "congress": [], "courses": [],
        "conference": [], "diploma": [], "certificate": [], "talk": [],
        "webinar": [], "workshops": [], "colloquium": [], "intership": [],

    }
    results_querys_plus = []
    separte_result = []
    keywords_search = read_conteiners()
    for plus in keywords_search:
        engine =Ask()
        search_query=f'{query} and {plus} and free after:2020-01-01 before:2021-01-01'
        results = engine.search(search_query, 20)
        results_querys_plus.append(results)
    key_c = 0
    for information in results_querys_plus:
        for item in information:
            datatime=find_date(item["link"]) if find_date(item["link"]) else ""
            print(datatime)
            dict_results[keywords_search[key_c]].append(
                {"title": item["title"], "link": item["link"], "text": item["text"]})
        key_c += 1
    return dict_results

file_keywords = open("search_engine/keywords.txt", "r")
for query in file_keywords:
    results = query_search(query.strip())
    insertDa = {"query": query.strip(), "results": results}
    insertDB = collection.insert_one(insertDa)
    print("----change----")
curson = collection.find({"query": "Earth observation"})
list_cur = list(curson)
