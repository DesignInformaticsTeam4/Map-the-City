from contextlib import closing
from flask_oauth import OAuth, OAuthException
from flask import Flask, request, session, render_template, redirect, url_for, g
import os
import json
import pickle
import sqlite3

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

# ====================================================================================================================
#                                                 dbms
# ====================================================================================================================

@app.route('/add_story/<story_name>')
def add_story(story_name):
    if session['twitter_user'] == 'kongaloosh':             # if the current user is admin
        cur = g.db.execute(                                 # get all the users
                """
                SELECT DISTINCT users.user_name
                FROM users
                """
            )

        for (user,) in cur.fetchall():                      # for each user
            g.db.execute(                                   # for add them to the begining of the story
                """
                INSERT INTO progression (user_name, story_name)
                values (?, ?)
                """, [user, story_name]
            )
            g.db.commit()
    return render_template('new_user.html')

# ====================================================================================================================
#                                                 dbms
# ====================================================================================================================

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def create_if_new_user(user_name, g):
    # try:
    cur = g.db.execute(
        """
            SELECT *
            FROM users
            WHERE user_name = '{name}'
        """.format(name=user_name))
    if cur.fetchall() == []:                    # if the user doesn't exist
        g.db.execute(                           # add the user
            """
                INSERT INTO users
                (user_name) VALUES (?)
            """,[user_name])
        g.db.commit()

        cur = g.db.execute(                     # get all current stories
            """
            SELECT DISTINCT progression.story_name
            FROM progression
            """
        )
        for (story_name,) in cur.fetchall():    # for all stories
            cur = g.db.execute(                 # insert the next story
                """
                    INSERT INTO progression
                    (user_name, story_name)
                    values (?, ?)
                """, [user_name, story_name]
            )
            g.db.commit()
            app.logger.info(story_name)
        return url_for('new_user')
    else:
        return url_for('welcome')
    # except sqlite3.OperationalError:
    #     raise NotImplementedError("you need to re-direct to an error page")
#
# ====================================================================================================================
#                                                 o auth setup
# ====================================================================================================================

twitter_config = pickle.load(open('keys/twitter/twitter.pkl','r'))

twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=twitter_config['consumer_key'],
    consumer_secret=twitter_config['consumer_secret']
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

# ====================================================================================================================
#                                     Basic templating and routing
# ====================================================================================================================

@app.route('/')
def index():
    """Index"""
    if session:
        locs = []
        with open('static/data/memories.json') as data_file:
            data = json.load(data_file)
            locs.append(data)
        if session and session['logged_in'] == True:
            app.logger.info(session['twitter_user'])
            app.logger.info(session)

        return render_template('index.html', locations=locs, data=open('static/data/memories.json').read().decode('utf-8'), session=session)
    else:
        return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')


# ====================================================================================================================
#                                                  data
# ====================================================================================================================

@app.route('/json-data/')
def json_data():
    """Separates the current story-line into the next point and the remaining points (to be unlocked)"""
    if session and session['logged_in']:
        cur = g.db.execute(                                         # Find the next point in the story
                    """
                        SELECT progression.point_number
                        FROM progression
                        WHERE progression.user_name = '{user_name}'
                        AND story_name = 'memories'
                    """.format(user_name=session['twitter_user'],),
                )
        (active_point,) = cur.fetchall()[0]                         # Parse the next point
        app.logger.info(active_point)
        data = open('static/data/memories.json').read()             # Open the current point
        parsed = json.loads(data)

        user_data = {}                                              # The data we're returning
        user_data['next_point'] = parsed[active_point]              # Add the next active point
        user_data['hidden_points'] = parsed[active_point:]          # Add the remaining points
        return json.dumps(user_data)
    return redirect('/')

@app.route('/u/user_data')
def user_view():
    if session and session['logged_in']:
        cur = g.db.execute(
            """
                SELECT progression.point_number
                FROM progression
                WHERE progression.user_name = '{user_name}'
                AND progression.story_name = 'memories'
            """.format(user_name = session['twitter_user'])
        )
        (active_point,) = cur.fetchall()[0]
        data = open('static/data/memories.json').read()             # Open the current point
        parsed = json.loads(data)
        user_data = {}                                              # The data we're returning
        user_data['next_point'] = parsed[active_point]              # Add the next active point
        user_data['passed_points'] = parsed[:-active_point]         # Add the remaining points
        return json.dumps(user_data)
    else:
        return redirect('/login')

@app.route('/story/<story_name>')
def story_name(story_name):
    """returns the data for a specific"""
    return NotImplementedError



# ====================================================================================================================
#                                           facebook oauth
# ====================================================================================================================

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


def pop_login_session():
    try: session.pop('logged_in', None)
    except KeyError: pass
    try: session.pop('facebook_token', None)
    except KeyError: pass
    try: session.pop('twitter_token', None)
    except KeyError: pass
    try: session.pop('twitter_user', None)
    except KeyError: pass

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))


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

# ====================================================================================================================
#                                               twitter oauth
# ====================================================================================================================

@app.route('/twitter_login')
def twitter_login():
    callback_url = url_for('twitter_authorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@app.route('/twitter_authorized')
@twitter.authorized_handler
def twitter_authorized(resp):
    try:
        next_url = request.args.get('next') or url_for('index')
        if resp is None:
            app.logger.info(resp)
            return redirect(next_url)

        session['logged_in'] = True;

        session['twitter_token'] = (
            resp['oauth_token'],
            resp['oauth_token_secret']
        )
        session['twitter_user'] = resp['screen_name']
        create_if_new_user(session['twitter_user'], g)
        app.logger.info('You were signed in as %s' % resp['screen_name'])
        return redirect(next_url)
    except OAuthException:
        redirect('/')


@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

# ====================================================================================================================
#                                               Basic Views
# ====================================================================================================================

@app.route('/u/<name>')
def user_page(name):
    """given some user id, find the stats of the user"""
    return None

@app.route('/new_user')
def new_user():
    render_template('new_user.html')


@app.route('/welcome_back')
def welcome():
    render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)