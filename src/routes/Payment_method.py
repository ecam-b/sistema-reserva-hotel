from flask import Blueprint, jsonify
# models and schemas
from models.Payment_methodModel import Payment_methodModel, Payment_methodSchema

for_him = Payment_methodSchema()
for_them = Payment_methodSchema(many=True)


payment_method_bp = Blueprint("payment_method", __name__)


@payment_method_bp.route("/", methods=["GET"])
def get_all_payment_method():
	try:
		payment_methods = Payment_methodModel.query.all()
		result = for_them.dump(payment_methods)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)})