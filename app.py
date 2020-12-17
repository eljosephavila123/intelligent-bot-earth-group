from flask import send_from_directory
import logging
import sys
import threading
from search_engine.main import *
from templates.src.connection_db import *
from flask import Flask, request, render_template, redirect, url_for
import os
app = Flask(__name__)

# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_query():
    if request.method == 'GET':
        query = request.args.get('query', '')
        try:
            results = search_database(query)
        except:
            input_new_queries(query)
            results = query_searchT(query)

        return render_template('search.html', programs=results["programs"], seminars=results["seminar"],
                               symposiums=results["symposium"], congress=results["congress"],
                               courses=results["courses"], conferences=results["conference"],
                               diplomas=results["diploma"], certificates=results["certificate"],
                               talks=results["talk"], webinars=results["webinar"],
                               workshops=results["workshops"], colloquiums=results["colloquium"],
                               interships=results["intership"])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()
