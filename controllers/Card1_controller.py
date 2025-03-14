from flask import Blueprint, jsonify, request
from models.Card1 import db, Card1

card1_bp = Blueprint("cards1", __name__)


@card1_bp.route("/api/cards", methods=["POST"])
def create_card():
    try:
        data = request.json
        new_card = Card1(
            order=data.get("order"),
            title=data.get("title"),
            description=data.get("description"),
            isComingSoon=data.get("isComingSoon", False),
            imgUrl=data.get("imgUrl"),
            display=data.get("display")
        )
        db.session.add(new_card)
        db.session.commit()
        return jsonify({"message": "Card created successfully!", "card": {
            "id": new_card.id,
            "type": new_card.type,
            "order": new_card.order,
            "title": new_card.title,
            "description": new_card.description,
            "isComingSoon": new_card.isComingSoon,
            "imgUrl": new_card.imgUrl,
            "display": new_card.display
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all cards
@card1_bp.route("/api/cards", methods=["GET"])
def get_cards():
    cards = Card1.query.all()
    result = [
        {
            "id": card.id,
            "type": card.type,
            "order": card.order,
            "title": card.title,
            "description": card.description,
            "isComingSoon": card.isComingSoon,
            "imgUrl": card.imgUrl,
            "display": card.display
        }
        for card in cards
    ]
    return jsonify({"cards": result}), 200


# Get a single card by ID
@card1_bp.route("/api/cards/<int:id>", methods=["GET"])
def get_card(id):
    card = Card1.query.get(id)
    if not card:
        return jsonify({"message": "Card not found"}), 404
    return jsonify(
        {
            "id": card.id,
            "type": card.type,
            "order": card.order,
            "title": card.title,
            "description": card.description,
            "isComingSoon": card.isComingSoon,
            "imgUrl": card.imgUrl,
            "display": card.display
        }
    ), 200


# Update a card by ID
@card1_bp.route("/api/cards/<int:id>", methods=["PUT"])
def update_card(id):
    card = Card1.query.get(id)
    if not card:
        return jsonify({"message": "Card not found"}), 404

    data = request.json
    card.title = data.get("title", card.title)
    card.order = data.get("order", card.order)
    card.description = data.get("description", card.description)
    card.isComingSoon = data.get("isComingSoon", card.isComingSoon)
    card.imgUrl = data.get("imgUrl", card.imgUrl)
    card.display = data.get("display", card.display)

    db.session.commit()
    return jsonify({"message": "Card updated successfully!"}), 200


# Delete a card by ID
@card1_bp.route("/api/cards/<int:id>", methods=["DELETE"])
def delete_card(id):
    card = Card1.query.get(id)
    if not card:
        return jsonify({"message": "Card not found"}), 404

    db.session.delete(card)
    db.session.commit()
    return jsonify({"message": "Card deleted successfully!"}), 200
