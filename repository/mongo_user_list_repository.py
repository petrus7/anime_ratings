from repository.repository_interface import RepositoryInterface


class MongoDBUserRepository(RepositoryInterface):

    def __init__(self, db):
        super(MongoDBUserRepository, self).__init__(db)
        self.users = self._db.db().users

    def get_user(self, user_name):
        return self.users.find_one({'username': user_name})

    def get_users(self, user_names):
        return self.users.find({'username': {'$in': user_names}})
