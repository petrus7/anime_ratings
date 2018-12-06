import logging
import os


class DevelopmentConfig(object):
    DEBUG = True
    MONGO_DB_URI = os.environ.get('MONGO_DB_URI', None)
    MONGO_DB_NAME = 'userslist.'
    LOG_LEVEL = logging.DEBUG
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_ORIGINS = r''
