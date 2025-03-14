from models import db


class Card1(db.Model):
    __tablename__ = 'card1'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), default="template1")
    order = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    isComingSoon = db.Column(db.Boolean, default=False)
    imgUrl = db.Column(db.String(500), nullable=True)
    display = db.Column(db.String(250), nullable=False)
