from flask import Blueprint, jsonify
# models and schemas
from models.HotelModel import HotelModel, HotelSchema

for_him = HotelSchema()
for_them = HotelSchema(many=True)


hotel_bp = Blueprint("hotel", __name__)


@hotel_bp.route("/", methods=["GET"])
def get_all_hotels():
	try:
		hotels = HotelModel.query.all()
		result = for_them.dump(hotels)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)}), 400