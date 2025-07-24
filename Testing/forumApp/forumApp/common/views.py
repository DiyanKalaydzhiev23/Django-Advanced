import asyncio
from pprint import pprint

from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.timezone import now
from django.views import View

from forumApp.common.tasks import _send_mail

UserModel = get_user_model()


def view_counter(request):
    pprint(dict(request.session))
    request.session['counter'] = request.session.get('counter', 0) + 1

    return HttpResponse(f"The count is {request.session.get('counter')}")


async def send_mail(*args):
    await _send_mail(*args)


async def notify_all_users(request):
    all_users = await sync_to_async(UserModel.objects.all)()
    users = await sync_to_async(list)(all_users)

    email_tasks = [
        send_mail(
            "Maintenance",
            "We are having a maintenance! Will be back shortly!",
            settings.DEFAULT_EMAIL,
            [user.email]
        ) for user in users
    ]

    await asyncio.gather(*email_tasks)


class SetTimeCookie(View):
    def get(self, request):
        return HttpResponse()

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        current_time = now()

        last_visit = request.COOKIES.get('last_visit')

        if last_visit:
            response.content = f"Your last visit was on {last_visit}".encode()
        else:
            response.content  = f"This is your first visit".encode()

        response.set_cookie(
            'last_visit',
            current_time.strftime("%Y-%m-%d %H:%M:%S")
        )

        return response
