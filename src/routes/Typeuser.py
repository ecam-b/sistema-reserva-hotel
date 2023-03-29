from flask import Blueprint, jsonify
# models and schemas
from models.TypeuserModel import TypeuserModel, TypeuserSchema

for_him = TypeuserSchema()
for_them = TypeuserSchema(many=True)


typeuser_bp = Blueprint("typeuser", __name__)

@typeuser_bp.route("/", methods=["GET"])
def get_all_typeusers():
	try:
		typeusers = TypeuserModel.query.all()
		result = for_them.dump(typeusers)
		jsonify(typeusers)
	except Exception as ex:
		return jsonify({"message": str(ex)}), 400