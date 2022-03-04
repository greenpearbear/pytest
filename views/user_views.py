from flask_restx import Resource, Namespace
from flask import request
from dao.model.user_model import UserSchema
from implemented import user_service
from helpers.decorators import admin_required

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self):
        all_users = user_service.get_all()
        return UserSchema(many=True).dump(all_users), 200

    def post(self):
        req_json = request.json
        new_user = user_service.post(req_json)
        return "", 201, {"location": f"/users/{new_user.id}"}


@users_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def get(self, uid: int):
        try:
            user = user_service.get_one(uid)
            return UserSchema().dump(user), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def put(self, uid: int):
        try:
            req_json = request.json
            user = user_service.put(uid, req_json)
            return UserSchema().dump(user), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def delete(self, uid: int):
        try:
            user_service.delete(uid)
            return "", 204
        except Exception as e:
            return str(e), 404
