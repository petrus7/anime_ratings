import abc


class RepositoryInterface(abc.ABC):

    def __init__(self, db):
        self._db = db

    @abc.abstractmethod
    def get_all_users_watched_anime(self, anime_id):
        pass


