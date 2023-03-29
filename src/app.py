from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# database
from database.db import db
# config
from config import SECRET_KEY, DATABASE_URI_CONNECTION
# routes
from routes import Typeuser, User, Payment_method, Payment, Hotel, Type_room, Room, Reservation


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
	app.register_blueprint(User.user_bp, url_prefix="/user")
	app.register_blueprint(Payment_method.payment_method_bp, url_prefix="/payment_method")
	app.register_blueprint(Payment.payment_bp, url_prefix="/payment")
	app.register_blueprint(Hotel.hotel_bp, url_prefix="/hotel")
	app.register_blueprint(Type_room.type_room_bp, url_prefix="/type_room")
	app.register_blueprint(Room.room_bp, url_prefix="/room")
	app.register_blueprint(Reservation.reservation_bp, url_prefix="/reservation")
	app.run(debug=True)