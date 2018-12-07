from api import db
from controller.user_data_fetcher import RestUserDataFetcher
from repository.mongo_user_list_repository import MongoDBUserListRepository


class ControllerFactory:

    @staticmethod
    def build_rest_mongo_controller():
        return RestUserDataFetcher(MongoDBUserListRepository(db))