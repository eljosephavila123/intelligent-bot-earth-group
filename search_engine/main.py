from .scrapper.search_engines import Ask
from .scrapper.search_engines.multiple_search_engines import MultipleSearchEngines, AllSearchEngines
from htmldate import find_date

def validate_date(test):
    document_y_or_n=test.split('/')[-1]
    pdf_y_or_n=test.split('.')[-1]
    if(pdf_y_or_n=='pdf' or document_y_or_n=='document'):
        return ''
    return find_date(test) if find_date(test) else ""


def read_conteiners():
    file_contents = open('search_engine/data.txt', 'r')
    return [linea.rstrip() for linea in file_contents]


def query_search(query):
    dict_results = {
        "programs": None, "seminar": None, "symposium": None, "congress": None, "courses": None,
        "conference": None, "diploma": None, "certificate": None, "talk": None,
        "webinar": None, "workshops": None, "colloquium": None, "intership": None,

    }
    results_querys_plus = []
    separte_result = []

    for plus in read_conteiners():
        engine = Ask()
        results = engine.search(query + " " + plus, 1)
        results_querys_plus.append(results)

    for information in results_querys_plus:
        information_individual = []
        for item in information:
            add_item = [item['title'], item['link'], item['text']]

            information_individual.append(add_item)
        separte_result.append(information_individual)
        information_individual = []
    position_query = 0
    for cheat in read_conteiners():

        dict_results[cheat] = separte_result[position_query]
        position_query += 1

    return dict_results


def query_searchT(query,after, before):
    
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
        search_query=f'{query} and {plus} and free after:{after} before:{before}'
        print(search_query)
        results = engine.search(search_query, 1)
        results_querys_plus.append(results)
    key_c = 0
    for information in results_querys_plus:
        for item in information:
            #datetime=validate_date(item["link"])
            dict_results[keywords_search[key_c]].append(
                {"title": item["title"], "link": item["link"], "text": item["text"]})
        key_c += 1
    return dict_results



