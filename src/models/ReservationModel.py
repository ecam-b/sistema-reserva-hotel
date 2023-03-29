from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class ReservationModel(db.Model):
	__tablename__ = "reservation"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
	start_date = db.Column(db.Date)
	end_date = db.Column(db.Date)
	total_price = db.Column(db.Numeric(10,2))


	def __init__(self, user_id, room_id, start_date, end_date, total_price):
		self.user_id = user_id
		self.room_id = room_id
		self.start_date = start_date
		self.end_date = end_date
		self.total_price = total_price


class ReservationSchema(ma.Schema):
	class Meta:
		fields = ("user_id", "room_id", "start_date", "end_date", "total_price")
