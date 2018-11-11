import os


class Configuration(object):
    DEBUG = True
    APP_DIR = os.path.dirname(os.path.realpath(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(APP_DIR, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "random string"
