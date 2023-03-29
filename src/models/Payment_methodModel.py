from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Payment_methodModel(db.Model):
	__tablename__ = payment_method


	id = db.Column(db.Integer, primary_key=True, nullable=True)
	name = db.Column(db.String(50))
	description = db.Column(db.String(100))
	commission = db.Column(db.Integer)
	email_contact = db.Column(db.String(100))


	def __init__(self, name, description, commission, email_contact):
		self.name = name
		self.description = description
		self.commission = commission
		self.email_contact = email_contact


class Payment_methodSchema(ma.Schema):
	class Meta:
		fields = ("name", "description", "commission", "email_contact")