from repository.repository_interface import RepositoryInterface


class MongoDBUserListRepository(RepositoryInterface):

    def __init__(self, db):
        super(MongoDBUserListRepository, self).__init__(db)
        self.lists = self._db.db().lists

    def get_user_animes(self, username):
        return self.lists.find({'username': username})

    def get_all_users_watched_anime(self, anime_id):
        pipeline = [
            {
                '$match': {'anime_id':anime_id}
            },
            {
                '$group': {
                    '_id': '$my_score',
                    'count': {'$sum': 1},
                    'users': {'$push': {'username':'$username','anime_id':'$anime_id','score':'$my_score'}}
                }
            },

        ]
        return self.lists.aggregate(pipeline)
