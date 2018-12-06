from repository.repository_interface import RepositoryInterface


class MongoDBUserListRepository(RepositoryInterface):

    def __init__(self, db):
        super(MongoDBUserListRepository, self).__init__(db)
        self.users = self._db.db().lists

    def get_user(self, user_name):
        return self.users.find_one({'username': user_name})

    def get_users(self, user_names):
        return self.users.find({'username': {'$in': user_names}})
