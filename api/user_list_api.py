from flask import Blueprint
from flask import jsonify
from flask import request
from flask_restful import Api, Resource

from api import db
from api.api_exception import BadParamsException
from controller.controllers_factory import ControllerFactory
from repository.mongo_user_list_repository import MongoDBUserListRepository

user_list_api = Blueprint('user_api', __name__)

api = Api(user_list_api)


class GetUser(Resource):

    def get(self):
        anime_id = request.args.get('anime_id', '')
        extreme_marker = request.args.get('greater', None)
        if anime_id is None or anime_id == '':
            raise BadParamsException('No anime id provided')
        if extreme_marker is not None and not isinstance(extreme_marker, bool):
            raise BadParamsException('extreme marker is not boolean')
        if not anime_id.isdigit():
            raise BadParamsException('anime id is not digit')

        c = ControllerFactory.build_rest_mongo_controller()
        return c.get_extremum_users(int(anime_id), extreme_marker)


class GetUserList(Resource):

    def get(self):
        username = request.args.get('username', None)
        if username is None or username == '':
            raise BadParamsException('Not username provided')
        c = ControllerFactory.build_rest_mongo_controller()
        return c.get_user_animes(username)

@user_list_api.errorhandler(BadParamsException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


api.add_resource(GetUser, '/get_users_extremum_users')
api.add_resource(GetUserList, '/get_user_anime_ids')
