from flask.json import jsonify
from flask.views import MethodView
from models.mentor import MentorCheck


class MentorCheckView(MethodView):
    def get(
        self,
    ):
        results = MentorCheck.query.all()
        return jsonify(results)
