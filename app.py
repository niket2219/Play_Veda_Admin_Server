from flask import Flask
from flask_cors import CORS
from config.config import Config
from models import db
from controllers.session_controller import session_bp
from controllers.Card1_controller import card1_bp
from controllers.Card2_controller import card2_bp
from flask import jsonify

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

app.register_blueprint(session_bp)
app.register_blueprint(card1_bp)
app.register_blueprint(card2_bp)


@app.route("/")
def home():
    return jsonify({"msg": "Hello"})


if __name__ == "__main__":
    app.run(debug=True)
