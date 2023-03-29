from flask import Blueprint, jsonify
# models and schemas
from models.ReservationModel import ReservationModel, ReservationSchema

for_him = ReservationSchema()
for_them = ReservationSchema(many=True)


reservation_bp = Blueprint("reservation", __name__)


@reservation_bp.route("/", methods=["GET"])
def get_all_reservations():
	try:
		reservations = ReservationModel.query.all()
		result = for_them.dump(reservations)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)})