import os


class AppConfig(object):
    SECRET_KEY = os.environ.get("APP_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class AppDevConfig(object):
    SECRET_KEY = os.environ.get("APP_KEY_DEV")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


def generate_herko_db_uri(driver):
    """
    Heroku create a non sqlchmey compatible uri which is rotated periodically.
    Generate a proper uri from this and include driver
    From postgres:// to postgresql+psycopg2://

    """
    if os.environ.get("APP_STATE") == "heroku":
        heroku_uri = os.environ.get("DATABASE_URL", "")
        _, uri = heroku_uri.split("://")
        driver_uri = f"postgresql+{driver}://{uri}"
        return driver_uri
    return ""


class AppHerokuConfig(object):
    """
    Heroku config to handle cases where heroku updates database uri
    Read configs from config variables in heroku
    """

    SECRET_KEY = os.environ.get("APP_KEY")
    SQLALCHEMY_DATABASE_URI = generate_herko_db_uri("psycopg2")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
