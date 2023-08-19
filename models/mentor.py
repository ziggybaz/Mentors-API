from .mixin import TimestampMixin
import uuid
from . import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass


@dataclass
class MentorCheck(db.Model, TimestampMixin):
    id: int
    cme_completion_date: str
    cme_unique_id: str
    county: str
    date_submitted: str
    drill_unique_id: str
    essential_cme_topic: bool
    essential_drill_topic: bool
    facility_code: str
    facility_name: str
    id_number_cme: str
    id_number_drill: str
    mentor_name: str
    submission_id: str
    success_story: str
    drill_topic: str
    cme_topic: str

    @property
    def drill_topic(self):
        return self.drill.topic

    @property
    def cme_topic(self):
        return self.cme.topic

    __tablename__ = "mentor_checklist"
    id = db.Column(db.Integer, primary_key=True)

    public_id = db.Column(
        db.String(150),
        index=True,
        default=uuid.uuid4,
        comment="For use when exposing record to public eg (API)",
    )
    cme_completion_date = db.Column(db.String(100))
    cme_unique_id = db.Column(
        db.Integer,
        db.ForeignKey("cme_topics.id"),
        nullable=False,
        index=True,
    )
    county = db.Column(db.String(150))
    date_submitted = db.Column(db.String(100))
    drill_unique_id = db.Column(
        db.Integer,
        db.ForeignKey("drill_topics.id"),
        nullable=False,
        index=True,
    )
    essential_cme_topic = db.Column(db.Boolean, default=False)
    essential_drill_topic = db.Column(db.Boolean, default=False)
    facility_code = db.Column(db.String(100))
    facility_name = db.Column(db.String(100))
    id_number_cme = db.Column(db.String(100))
    id_number_drill = db.Column(db.String(100))
    mentor_name = db.Column(db.String(100))
    submission_id = db.Column(db.String(100))
    success_story = db.Column(db.String(250))

    def __init__(
        self,
        /,
        cme_completion_date,
        cme_unique_id,
        county,
        date_submitted,
        drill_unique_id,
        essential_cme_topic,
        essential_drill_topic,
        facility_code,
        facility_name,
        id_number_cme,
        id_number_drill,
        mentor_name,
        submission_id,
        success_story,
    ):
        self.cme_completion_date = cme_completion_date

        self.cme_unique_id = cme_unique_id
        self.county = county
        self.date_submitted = date_submitted
        self.drill_unique_id = drill_unique_id
        self.essential_cme_topic = essential_cme_topic
        self.essential_drill_topic = essential_drill_topic
        self.facility_code = facility_code
        self.facility_name = facility_name
        self.id_number_cme = id_number_cme
        self.id_number_drill = id_number_drill
        self.mentor_name = mentor_name
        self.submission_id = submission_id
        self.success_story = success_story

    @hybrid_property
    def not_deleted(self):
        return self.deleted_at is None

    def __repr__(self):
        return f"<MentorCheck {self.public_id}>"
