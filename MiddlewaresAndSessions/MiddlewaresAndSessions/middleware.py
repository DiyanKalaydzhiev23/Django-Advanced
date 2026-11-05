from datetime import timezone
from time import time

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now


class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time()

    def process_response(self, request, response):
        print(f'{request.method} {request.path} - {now(): Executed in {time() - self.start_time}}')
        return response


class TotalRequestsMiddleware(MiddlewareMixin):
    total_requests = 0

    def process_request(self, request):
        TotalRequestsMiddleware.total_requests += 1

    def process_response(self, request, response):
        response['X-Total-Requests'] = TotalRequestsMiddleware.total_requests
        return response


class IPWhitelistingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        client_ip = request.META.get('REMOTE_ADDR', '')  # 127.0.0.1

        if client_ip not in settings.ALLOWED_IPS:
            return HttpResponseForbidden('Access denied for this IP address!')


class SessionRateMiddleware(MiddlewareMixin):
    SESSION_KEY = 'rate_limit_logs'
    window_seconds = 60

    def process_request(self, request):
        _now = now().timestamp()
        window_start = _now - self.window_seconds

        recent_requests = [
            t for t in request.session.get(self.SESSION_KEY, [])
            if t > window_start
        ]

        if len(recent_requests) >= settings.REQUESTS_PER_MINUTE:
            return HttpResponse("Too many requests!", status=429)

        recent_requests.append(_now)
        request.session[self.SESSION_KEY] = recent_requests
