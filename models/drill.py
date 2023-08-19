from .mixin import TimestampMixin
from . import db


class DrillTopic(db.Model, TimestampMixin):
    __tablename__ = "drill_topics"
    id = db.Column(db.Integer, primary_key=True)

    topic = db.Column(db.String(150), unique=True, index=True, nullable=False)
    mentorships = db.relationship(
        "MentorCheck",
        backref="drill",
        lazy="joined",
    )

    def __init__(self, topic):
        self.topic = topic

    def __repr__(self):
        return f"<DrillTopic {self.id}>"
