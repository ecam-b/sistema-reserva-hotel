from flask import Blueprint, jsonify
# models and schemas
from models.Type_roomModel import Type_roomModel, Type_roomSchema

for_him = Type_roomSchema()
for_them = Type_roomSchema(many=True)


type_room_bp = Blueprint("type_room", __name__)


@type_room_bp.route("/", methods=["GET"])
def get_all_type_rooms():
	try:
		type_rooms = Type_roomModel.query.all()
		result = for_them.dump(type_rooms)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)}) 