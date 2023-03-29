from flask import Blueprint, jsonify
# models and schemas
from models.PaymentModel import PaymentModel, PaymentSchema

for_him = PaymentSchema()
for_them = PaymentSchema(many=True)


payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/", methods=["GET"])
def get_all_payments():
	try:
		payments = PaymentModel.query.all()
		result = for_them.dump(payments)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)}), 400