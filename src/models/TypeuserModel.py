from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TypeuserModel(db.Model):
	__tablename__ = "typeuser"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	description = db.Column(db.String(50), unique=True)
	users = db.relationship("UserModel", backref="typeuser" lazy=True)


	def __init__(self, description):
		self.description = description


class TypeuserSchema(ma.Schema):
	class Meta:
		fields = ("id", "description")

