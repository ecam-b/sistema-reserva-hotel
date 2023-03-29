from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Type_roomModel(db.Model):
	__tablename__ = "type_room"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	description = db.Column(db.String(100), unique=True)
	rooms = db.relationship("RoomModel", backref="type_room", lazy=True)


	def __init__(self, description):
		self.description = description


class Type_roomSchema(ma.Schema):
	class Meta:
		fields = ("description",)