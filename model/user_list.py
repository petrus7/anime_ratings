import json


class User:

    def __init__(self, db_user_entity: dict):

        self.username = db_user_entity.get('username') if db_user_entity.get('username') else ''
        self.user_id = db_user_entity.get('user_id') if db_user_entity.get('user_id') else 0
        self.gender = db_user_entity.get('gender') if db_user_entity.get('gender') else ''
        self.location = db_user_entity.get('location') if db_user_entity.get('location') else ''

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__


