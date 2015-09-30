
from flask import Flask, request, session, render_template
import os
import json

__author__ = 'kongaloosh'

# configuration
DATABASE = 'kongaloosh.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['STATIC_FOLDER'] = os.getcwd()
cfg = None


@app.route('/')
def index():
    locs = []
    with open('static/data/memories.json') as data_file:
        data = json.load(data_file)
        locs.append(data)
    return render_template('index.html', locations=locs, data=open('static/data/memories.json').read().decode('utf-8') )


@app.route('/json-data/')
def json_data():
        return open('static/data/memories.json').read()

if __name__ == "__main__":
    app.run(debug=True)