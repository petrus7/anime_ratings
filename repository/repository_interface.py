import abc


class RepositoryInterface(abc.ABC):

    def __init__(self, db):
        self._db = db

    @abc.abstractmethod
    def get_user(self, user_name):
        pass

    @abc.abstractmethod
    def get_users(self, user_names):
        pass
