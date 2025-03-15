from models import db
from sqlalchemy.dialects.postgresql import JSONB


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(255), nullable=False)
    ageGroup = db.Column(db.String(255))
    batchSize = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    benefitsDesc = db.Column(db.String(500))
    benefits = db.Column(JSONB, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    sessionActivities = db.Column(JSONB, nullable=False, default=[])
