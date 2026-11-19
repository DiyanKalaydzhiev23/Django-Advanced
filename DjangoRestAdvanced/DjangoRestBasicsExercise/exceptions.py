from django.http import Http404
from rest_framework.views import exception_handler


def log_404_exception(exc, context):
    if isinstance(exc, Http404):
        print("There was a 404 on our app!")

    return exception_handler(exc, context)