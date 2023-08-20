from flask import Flask
import os
from .api import api_v1
from conf import AppConfig, AppDevConfig, AppHerokuConfig
from flasgger import Swagger
from models import MentorCheck
from models import CMETopic
from models import DrillTopic


def init_app(db=None):
    app = Flask(__name__)
    app_state = os.environ.get("APP_STATE")
    if app_state == "dev" or not app_state:
        app.config.from_object(AppDevConfig)
    elif app_state == "docker":
        app.config.from_object(AppConfig)
    elif app_state == "heroku":
        app.config.from_object(AppHerokuConfig)
    if db:
        db.init_app(app)

    swag = Swagger(app, template_file="./docs/docs.yml")
    app.register_blueprint(api_v1)
    return app
