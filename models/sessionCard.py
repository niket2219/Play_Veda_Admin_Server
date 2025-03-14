from models import db
from sqlalchemy.dialects.postgresql import JSONB


class LilaCard(db.Model):
    __tablename__ = "Lila_Card"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    subtitle = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), default="template2")
    order = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    details_button = db.Column(db.String(255), nullable=False)
    images = db.Column(JSONB, nullable=True, default=[])
    display = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON responses."""
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "type": self.type,
            "order": self.order,
            "location": self.location,
            "details_button": self.details_button,
            "images": self.images,
            "display": self.display
        }
