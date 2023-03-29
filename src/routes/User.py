from flask import Blueprint, jsonify
# models and schemas
from models.UserModel import UserModel, UserSchema

for_him = UserSchema()
for_them = UserSchema(many=True)


user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def get_all_users():
	try:
		users = UserModel.query.all()
		result = for_them.dump(users)
		return jsonify(result)
	except Exception as ex:
		return jsonify({"message": str(ex)}), 400