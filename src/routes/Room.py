from flask import Blueprint, jsonify
# models and schemas
from models.RoomModel import RoomModel, RoomSchema

for_him = RoomSchema()
for_them = RoomSchema(many=True)


room_bp = Blueprint("room", __name__)


@room_bp.route("/", methods=["GET"])
def get_all_rooms():
	try:
		rooms = RoomModel.query.all()
		result = for_them.dump(rooms)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)})