from datetime import timedelta
from functools import wraps
from flask import Flask, url_for, redirect, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from authlib.integrations.flask_client import OAuth
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config()):
  """App factory for creating flask app"""
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(config_class)
  # Create all of the models that are subclassed from db.Model
  db.app = app
  ma.init_app(app)
  db.init_app(app)

  # Authlib
  oauth = OAuth(app)
  if not app.config['TESTING']:
    oauth.register(
      name='google',
      # use os env for this
      client_id=config_class.GOOGLE_OAUTH_CLIENT_ID,
      client_secret=config_class.GOOGLE_OAUTH_CLIENT_SECRET,
      access_token_url='https://accounts.google.com/o/oauth2/token',
      access_token_params=None,
      base_url='http://127.0.0.1:5000',
      authorize_url='https://accounts.google.com/o/oauth2/auth',
      authorize_params=None,
      api_base_url='https://www.googleapis.com/oauth2/v1/',
      # This is only needed if using openId to fetch user info
      userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
      client_kwargs={'scope': 'openid email profile'},
      jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
    )
  app.oauth = oauth
 
  with app.app_context():
    from .blueprints import show_blueprint, person_blueprint, user_blueprint, app_blueprint
    from .models import Show, ShowCast, ShowCategory, ShowCountry, ShowDirector, Category, Country, Person
    app.register_blueprint(show_blueprint.shows)
    app.register_blueprint(person_blueprint.actors)
    app.register_blueprint(person_blueprint.directors)
    app.register_blueprint(user_blueprint.auth)
    app.register_blueprint(app_blueprint.app_blueprint)
    db.create_all()

    return app

def login_required(func):
  """Login decorator to ensure routes have correct permissions."""
  @wraps(func)
  def decorated_function(*args, **kwargs):
    user = dict(session).get('profile', None)
    # You would add a check here and usethe user id or something to fetch
    # the other data for that user/check if they exist
    if user:
      return func(*args, **kwargs)
    return redirect(url_for('auth.login'))
  return decorated_function
