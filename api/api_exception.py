from base_exception import BaseWebException


class BadParamsException(BaseWebException):
    status_code = 400