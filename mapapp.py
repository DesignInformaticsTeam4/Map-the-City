from flask_oauth import OAuth
from flask import Flask, request, session, render_template, redirect, url_for
import os
import json
import pickle

__author__ = 'kongaloosh'

# configuration
DATABASE = 'kongaloosh.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['STATIC_FOLDER'] = os.getcwd()
app.config['SECRET_KEY'] = 'pamplemousse'
cfg = None

oauth = OAuth()

twitter_config = pickle.load(open('keys/twitter/twitter.pkl','r'))

twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=twitter_config['consumer_key'],
    consumer_secret=twitter_config
)

facebook_config = pickle.load(open('keys/facebook/facebook.pkl','r'))

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=facebook_config['id'],
    consumer_secret=facebook_config['secret'],
    request_token_params={'scope': ('email, ')}
)

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


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)


@app.route("/facebook_login")


@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)