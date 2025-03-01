from flask import request, jsonify, Blueprint
from models import db
from models.sessionCard import LilaCard

lilaCard_bp = Blueprint("LilaCard", __name__)


@lilaCard_bp.route("/api/cards2", methods=["POST"])
def create_location():
    data = request.json
    new_entry = LilaCard(
        location=data.get("location"),
        details_button=data.get("details_button"),
        images=data.get("images", [])
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Location added", "data": new_entry.to_dict()}), 201


# 🔹 **Get all records**
@lilaCard_bp.route("/api/cards2", methods=["GET"])
def get_all_locations():
    cards = LilaCard.query.all()
    return jsonify([loc.to_dict() for loc in cards]), 200


# 🔹 **Get a single record by ID**
@lilaCard_bp.route("/api/cards2/<int:id>", methods=["GET"])
def get_location(id):
    cards = LilaCard.query.get_or_404(id)
    return jsonify(cards.to_dict()), 200


# 🔹 **Update a record**
@lilaCard_bp.route("/api/cards2/<int:id>", methods=["PUT"])
def update_location(id):
    cards = LilaCard.query.get_or_404(id)
    data = request.json

    cards.location = data.get("location", cards.location)
    cards.details_button = data.get(
        "details_button", cards.details_button)
    cards.images = data.get("images", cards.images)

    db.session.commit()
    return jsonify({"message": "Location updated", "data": cards.to_dict()}), 200


# 🔹 **Delete a record**
@lilaCard_bp.route("/api/cards2/<int:id>", methods=["DELETE"])
def delete_location(id):
    location = LilaCard.query.get_or_404(id)
    db.session.delete(location)
    db.session.commit()
    return jsonify({"message": "Location deleted"}), 200
