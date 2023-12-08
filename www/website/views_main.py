import flask
from . import mysqldbc

views = flask.Blueprint('views_main', __name__)



# Home
@views.route('/')
def home():

  with mysqldbc.MySQLdbConnection() as db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM `contacts`')
    data = cursor.fetchall()

  return flask.render_template('index.html', contacts = data)
