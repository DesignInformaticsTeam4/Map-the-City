
from flask import Flask, request, session, render_template
import os

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
    return render_template('stuff.html')


if __name__ == "__main__":
    app.run(debug=True)