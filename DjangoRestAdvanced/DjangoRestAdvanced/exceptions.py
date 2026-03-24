from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        return Response({
                'detail': 'Hey there ' + exc.args[0].lower(),
            }, status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(exc, PermissionDenied):
        return Response({
                'detail': f"Access denied. You can't access this endpoint in the garage api",
            }, status=status.HTTP_404_NOT_FOUND,
        )

    return exception_handler(exc, context)