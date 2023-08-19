from models import db
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return db.Column(
            db.DateTime,
            server_default=func.now(),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, onupdate=func.now())

    @declared_attr
    def deleted_at(cls):
        return db.Column(db.DateTime, nullable=True)
