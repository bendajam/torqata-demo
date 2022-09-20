from datetime import timedelta
import os

class Config(object):
  """Config class"""
  SESSION_COOKIE_NAME = 'google-login-session'
  PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
  TESTING = False

  @property
  def SQLALCHEMY_DATABASE_URI(self):
    DB_USER = os.getenv("TORQATA_DB_USER")
    DB_PASS = os.getenv("TORQATA_DB_PASS")
    return f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/torqata"

  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'secret garden'

  GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
  GOOGLE_OAUTH_CLIENT_SECRET= os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')
  
# '14474533764-05qds5reeesgsu8bj5008fjmc3n5o24g.apps.googleusercontent.com',
# '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',