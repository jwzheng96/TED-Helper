import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:20000831@localhost:5432/ted'
    SQLALCHEMY_TRACK_MODIFICATIONS = False