from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserModel(db.Model):
	__tablename__ = "user"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	private_id = db.Column(db.String(36), nullable=False, unique=True)
	username = db.Column(db.String(50), unique=True)
	name = db.Column(db.String(100))
	gmail = db.Column(db.String(100))
	password = db.Column(db.String(300))
	phone = db.Column(db.String(12))
	typeuser_id = db.Column(db.Integer, db.ForeignKey("typeuser.id"), nullable=False)
	reservations = db.relationship("ReservationModel", backref="user", lazy=True)


	def __init__(self, private_id, username, name, gmail, password, phone, typeuser_id):
		self.private_id = private_id
		self.username = username
		self.name = name
		self.gmail = gmail
		self.passowrd = passowrd
		self.phone = phone
		self.typeuser_id = typeuser_id


class UserSchema(ma.Schema):
	class Meta:
		fields = ("username", "name", "gmail", "phone", "typeuser_id")