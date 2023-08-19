import os


class AppConfig(object):
    SECRET_KEY = os.environ.get("APP_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class AppDevConfig(object):
    SECRET_KEY = os.environ.get("APP_KEY_DEV")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
