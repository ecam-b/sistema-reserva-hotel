from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class HotelModel(db.Model):
	__tablename__ = "hotel"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(50), unique=True)
	address = db.Column(db.String(100), unique=True)
	phone = db.Column(db.String(12))
	email_contact = db.Column(db.String(100))


	def __init__(self, name, address, phone, email_contact):
		self.name = name
		self.address = address
		self.phone = phone
		self.email_contact = email_contact


class HotelSchema(ma.Schema):
	class Meta:
		fields = ("name", "address", "phone", "email_contact")