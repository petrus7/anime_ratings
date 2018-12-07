import json


class UserList:

    def __init__(self, db_user_entity: dict):
        self.username = db_user_entity.get('username') if db_user_entity.get('username') else ''
        self.anime_id = db_user_entity.get('anime_id') if db_user_entity.get('anime_id') else 0
        self.score = db_user_entity.get('score') if db_user_entity.get('score') else ''

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__


class UserListStorage:

    def __init__(self, **kwargs):
        self.u_data = []
        self.additional_options = dict(kwargs)

    def get_most_extreme_users(self,user_groups, positive: bool=True):
        user_groups = list(user_groups)
        if positive:
            self.u_data = [UserList(u) for u in user_groups[-1].get('users')]
        else:
            self.u_data = [UserList(u) for u in user_groups[0].get('users')]

    def to_dict(self):
        return [u.to_dict() for u in self.u_data]