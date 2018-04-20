from flask_restful import Resource, reqparse, inputs, abort
from models.user import UserModel
from security import jwt_required

class User(Resource):
    @jwt_required()
    def get(self, _id=None):
        if _id:
            user = UserModel.find_by_id(_id)

            if not user:
                return {'message': 'no results'}, 204
            return user.json(), 200

        users = UserModel.all()

        if not users:
            return {'message': 'no results'}, 204
        return [user.json() for user in users], 200

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        data = parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user:
            abort(400, message='User is already registered')

        user = UserModel(**data)
        user.save_to_db()

        return data, 200
