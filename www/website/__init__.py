import flask

# Relative imports from top level of this package
from . import views_main
from . import views_contacts

def create_app():
  app = flask.Flask(__name__)
  app.secret_key = 'loremipsumdolorsiamet'

  app.register_blueprint(views_main.views, url_prefix='/')
  app.register_blueprint(views_contacts.views, url_prefix='/')

  return app
