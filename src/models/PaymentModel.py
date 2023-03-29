from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PaymentModel(db.Model):
	__tablename__ = "payment"


	id = db.Column(db.Integer, primary_key=True, nullable=False)
	reservation_id = db.Column(db.Integer, db.ForeingKey("reservation.id"), nullable=False)
	date_payment = db.Column(db.Date, default=date.today)
	amount_payment = db.Column(db.Numeric(10,2), nullable=False)
	payment_method_id = db.Column(db.Integer, db.ForeingKey("payment_method.id"), nullable=False)


	def __init__(self, reservation_id, date_payment, amount_payment, payment_method_id):
		self.reservation_id = reservation_id
		self.date_payment = date_payment
		self.amount_payment = amount_payment
		self.payment_method_id = payment_method_id


class PaymentSchema(ma.Schema):
	class Meta:
		fields = ("reservation_id", "date_payment", "amount_payment", "payment_method_id")
