from rest_framework.exceptions import APIException


class InvalidTokenException(APIException):
    status_code = 498
    default_detail = 'Invalid token!'
