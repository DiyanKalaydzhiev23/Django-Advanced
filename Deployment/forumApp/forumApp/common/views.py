from pprint import pprint

from django.http import HttpResponse
from django.utils.timezone import now
from django.views import View


def view_counter(request):
    pprint(dict(request.session))
    request.session['counter'] = request.session.get('counter', 0) + 1

    return HttpResponse(f"The count is {request.session.get('counter')}")


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
