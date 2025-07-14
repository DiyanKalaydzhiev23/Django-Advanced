from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.exceptions import InvalidTokenException


@api_view(['POST'])
def check_token(request):
    token = request.data.get('token')

    try:
        db_token = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise InvalidTokenException()
        # return Response(
        #     data={"detail": "Token is invalid."},
        #     status=498,
        # )

    return Response(
        status=status.HTTP_200_OK,
    )