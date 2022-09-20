from flask import Flask, url_for, redirect, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from authlib.integrations.flask_client import OAuth
from datetime import timedelta
from functools import wraps

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
  app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
  app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:letmein@localhost:5432/torqata"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.secret_key = 'secrete garden'
  # Create all of the models that are subclassed from db.Model
  db.app = app
  ma.init_app(app)
  db.init_app(app)

  # Authlib
  oauth = OAuth(app)
  oauth.register(
    name='google',
    # use os env for this
    client_id='14474533764-05qds5reeesgsu8bj5008fjmc3n5o24g.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    base_url='http://127.0.0.1:5000',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
  )
  app.oauth = oauth
 
  with app.app_context():
    from .blueprints import show_blueprint, person_blueprint, user_blueprint, app_blueprint
    app.register_blueprint(show_blueprint.shows)
    app.register_blueprint(person_blueprint.actors)
    app.register_blueprint(person_blueprint.directors)
    app.register_blueprint(user_blueprint.auth)
    app.register_blueprint(app_blueprint.app_blueprint)
    from .models import Show, ShowCast, ShowCategory, ShowCountry, ShowDirector, Category, Country, Person
    db.create_all()

    return app

def login_required(func):
  @wraps(func)
  def decorated_function(*args, **kwargs):
    user = dict(session).get('profile', None)
    # You would add a check here and usethe user id or something to fetch
    # the other data for that user/check if they exist
    if user:
      return func(*args, **kwargs)
    return redirect(url_for('auth.login'))
  return decorated_function
