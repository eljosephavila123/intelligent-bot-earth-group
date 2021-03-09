import logging
import sys
import threading
from search_engine.main import *
from templates.src.connection_db import *
from flask import Flask, request, render_template, redirect, url_for,session,send_from_directory
import os
import datetime

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)


@app.route('/', methods=['GET','POST'])
def index():
    today = datetime.datetime.utcnow()
    before = today - datetime.timedelta(days=365)
    return render_template('index.html',today=today,before=before, keywords=get_keywords_db())

@app.route('/keywords',methods=['GET'])
def get_keywords():
    return ''

@app.route('/search', methods=['GET','POST'])
def search_query():
    if request.method == 'GET':
        query = request.args.get('query', '')
        today = request.args.get('startdate', '')
        before= request.args.get('enddate','')
        try:
            results = search_database(query)
        except:
            input_new_queries(query)
            results = query_searchT(query,today,before)
        return render_template('search.html', 
        programs=results["programs"], seminars=results["seminar"],
        symposiums=results["symposium"], congress=results["congress"],
        courses=results["courses"], conferences=results["conference"],
        diplomas=results["diploma"], certificates=results["certificate"],
        talks=results["talk"], webinars=results["webinar"],
        workshops=results["workshops"], colloquiums=results["colloquium"],
        interships=results["intership"] ,)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()


