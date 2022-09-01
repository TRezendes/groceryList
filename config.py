import os
from dotenv import load_dotenv

#basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv('.flaskenv')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.environ.get('FLASK_ENV')
    ENV = os.environ.get('FLASK_ENV')
    
class DevConfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    DEBUG = True
    TEST = False
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
    SERVER_NAME = os.environ.get('SERVER_NAME')
    DEBUG = False
    TEST = False
    
class TestConfig(Config):
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    DEBUG = True
    TEST = True