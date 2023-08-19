from flask import Flask
from .api import api_v1


def init_app(db=None):
    app = Flask(__name__)
    if db:
        db.init_app(app)

    app.register_blueprint(api_v1)
    return app
