from flask import Flask
import os
from .api import api_v1
from conf import AppConfig, AppDevConfig
from models.mentor import MentorCheck
from models.cme import CMETopic
from models.drill import DrillTopic


def init_app(db=None):
    app = Flask(__name__)
    app_state = os.environ.get("APP_STATE")
    if app_state == "dev" or not app_state:
        app.config.from_object(AppDevConfig)
    if app_state == "prod":
        app.config.from_object(AppConfig)
    if db:
        db.init_app(app)

    app.register_blueprint(api_v1)
    return app
