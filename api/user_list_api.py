from flask import Blueprint
from flask.json import jsonify
from flask_restful import Api, Resource
from flask import request
from api.api_exception import BadParamsException
from repository.mongo_user_list_repository import MongoDBUserListRepository

user_api = Blueprint('user_api', __name__)

api = Api(user_api)



class GetUserList(Resource):

    def get(self):
        return f'alamakota'






# # @user_api.errorhandler(DBException)
# @user_api.errorhandler(BadParamsException)
# def handle_invalid_usage(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response


api.add_resource(GetUserList, '/get_user')
# api.add_resource(GetUsersById, '/get_anime_by_id')