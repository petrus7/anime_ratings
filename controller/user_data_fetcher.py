from model.user_list import UserListStorage
from repository.repository_interface import RepositoryInterface


class RestUserDataFetcher:

    def __init__(self, repository: RepositoryInterface):
        self.r = repository

    def get_extremum_users(self, anime_id: int, positive:bool=True):
        users_group = self.r.get_all_users_watched_anime(anime_id)
        um = UserListStorage()
        um.get_most_extreme_users(users_group, positive)
        return um.to_dict()
