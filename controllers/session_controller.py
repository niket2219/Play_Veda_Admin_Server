from flask import request, jsonify, Blueprint
from models import db
from models.session import Session

session_bp = Blueprint("name", __name__)

# Create a new session


def create_session():
    try:
        theme = request.json.get("theme")
        ageGroup = request.json.get("ageGroup")
        batchSize = request.json.get("batchSize")
        duration = request.json.get("duration")
        benefitsDesc = request.json.get("benefitsDesc")
        benefits = request.json.get("benefits", [])
        date = request.json.get("date")
        day = request.json.get("day")
        time = request.json.get("time")
        month = request.json.get("month")
        week = request.json.get("week")
        location = request.json.get("location")
        sessionActivities = request.json.get(
            "sessionActivities", [])

        new_session = Session(
            theme=theme,
            ageGroup=ageGroup,
            batchSize=batchSize,
            duration=duration,
            benefitsDesc=benefitsDesc,
            benefits=benefits,
            date=date,
            day=day,
            time=time,
            month=month,
            week=week,
            location=location,
            sessionActivities=sessionActivities
        )

        db.session.add(new_session)
        db.session.commit()

        return jsonify({"message": "Session created successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


def update_session(session_id):
    try:
        session = Session.query.get(session_id)

        if not session:
            return jsonify({"message": "Session not found"}), 404

        data = request.json

        session.theme = data.get("theme", session.theme)
        session.ageGroup = data.get("ageGroup", session.ageGroup)
        session.batchSize = data.get("batchSize", session.batchSize)
        session.duration = data.get("duration", session.duration)
        session.benefitsDesc = data.get("benefitsDesc", session.benefitsDesc)
        session.benefits = data.get("benefits", session.benefits)
        session.date = data.get("date", session.date)
        session.day = data.get("day", session.day)
        session.time = data.get("time", session.time)
        session.month = data.get("month", session.month)
        session.week = data.get("week", session.week)
        session.location = data.get("location", session.location)
        session.sessionActivities = data.get(
            "sessionActivities", session.sessionActivities)

        db.session.commit()

        return jsonify({"message": "Session updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all sessions
def get_sessions():
    sessions = Session.query.all()
    result = []

    for session in sessions:
        activities = session.sessionActivities

        result.append({
            "id": session.id,
            "theme": session.theme,
            "benefitsDesc": session.benefitsDesc,
            "benefits": session.benefits,
            "date": session.date,
            "day": session.day,
            "time": session.time,
            "month": session.month,
            "week": session.week,
            "location": session.location,
            "sessionActivities": activities
        })

    return jsonify({"sessions": result}), 200


# Delete session
def delete_session(session_id):
    session = Session.query.get(session_id)
    if not session:
        return jsonify({"message": "Session not found"}), 404

    db.session.delete(session)
    db.session.commit()
    return jsonify({"message": "Session deleted successfully!"}), 200


@session_bp.route("/api/sessions", methods=["POST"])
def create_session_route():
    return create_session()


@session_bp.route("/api/sessions", methods=["GET"])
def get_sessions_route():
    return get_sessions()


@session_bp.route("/api/sessions/update/<int:id>", methods=["PUT"])
def update_session_route(id):
    return update_session(id)


@session_bp.route("/api/sessions/<int:id>", methods=["DELETE"])
def delete_session_route(id):
    return delete_session(id)
