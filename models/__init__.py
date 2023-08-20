from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cme import CMETopic
from .drill import DrillTopic
from .mentor import MentorCheck
