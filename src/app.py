from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# database
from database.db import db
# config
from config import SECRET_KEY, DATABASE_URI_CONNECTION
# routes
from routes import Typeuser


app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
Marshmallow(app)


db.init_app(app)
with app.app_context():
	db.create_all()


if __name__ == "__main__":
	# blueprints
	app.register_blueprint(Typeuser.typeuser_bp, url_prefix="/typeuser")
	app.run(debug=True)