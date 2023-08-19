from flask.json import jsonify
from flask.views import MethodView


class PingView(MethodView):

    def get(self):

        message = {"isAlive": True}
        return jsonify(message)
