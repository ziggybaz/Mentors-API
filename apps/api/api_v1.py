from flask import Blueprint
from .views.ping import PingView


api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api_v1.add_url_rule("/ping", view_func=PingView.as_view("ping"))