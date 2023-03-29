from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class RoomModel(db.Model):
	__tablename__ = "room"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.id"), nullable=False)
	type_room_id = db.Column(db.Integer, db.ForeignKey("type_room.id"), nullable=False)
	number_beds = db.Column(db.Integer)
	price = db.Column(db.Numeric(10,2), nullable=False)
	floor = db.Column(db.Integer)
	reservations = db.relationship("ReservationModel", backref="room", lazy=True)


	def __init__(self, hotel_id, type_room_id, number_beds, price, floor):
		self.hotel_id = hotel_id
		self.type_room_id = type_room_id
		self.number_beds = number_beds
		self.price = price
		self.floor = floor


class RoomSchema(ma.Schema):
	class Meta:
		fields = ("hotel_id", "type_room_id", "number_beds", "price", "floor")