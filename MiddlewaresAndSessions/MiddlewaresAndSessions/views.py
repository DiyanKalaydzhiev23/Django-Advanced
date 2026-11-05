from http.client import responses

from django.conf import settings
from django.contrib.auth import logout
from django.core.signing import Signer, BadSignature
from django.http import HttpResponse
from django.shortcuts import render, redirect


def choose_language(request) -> HttpResponse:
    if request.method == "POST":
        selected_language = request.POST.get('language', '').lower()

        if selected_language in settings.SUPPORTED_LANGUAGES:
            request.session["language"] = selected_language

        return redirect('home')


def home(request) -> HttpResponse:
    GREETINGS_MESSAGES = {
        "en": "Hello!",
        "de": "Hallo!",
        "bg": "Здравей!",
    }

    current_language = request.session.get("language", 'en')
    greeting_message = GREETINGS_MESSAGES.get(current_language)

    role_cookie = request.COOKIES.get('role', '')
    signature_valid = False
    signer = Signer()

    try:
        verified_value = signer.unsign(role_cookie)
        signature_valid = True
    except BadSignature:
        verified_value = "Invalid signature"

    return render(
        request,
        'home_page.html',
        {
            'remaining_seconds': request.session.get_expiry_age(),
            "current_language": current_language,
            "greeting_message": greeting_message,
            "supported_languages": settings.SUPPORTED_LANGUAGES,
            'signature_valid': signature_valid,
            'verified_value': verified_value
        }
    )


def session_expiry(request) -> HttpResponse:
    error_message = ''

    if request.method == "POST":
        expiry_value = request.POST.get('expiry_seconds', 0)

        try:
            expiry_seconds = int(expiry_value)
        except ValueError:
            error_message = "Enter a positive number"
        else:
            request.session.set_expiry(expiry_seconds)
            return redirect('home')

    return render(
        request,
        'home_page.html',
        {
            'remaining_seconds': request.session.get_expiry_age(),
            'error_message': error_message
        }
    )

def flush_session(request):
    if request.method == "POST":
        request.session.flush()
    return redirect('home')


def set_signed_cookie(request):
    signer = Signer()  # sha256 -> value+SECRET_KEY
    signed_value = signer.sign('standard_user')  # standard_user:4ibfweqru734v7348
    response = redirect('home')
    response.set_cookie(
        key='role',
        value=signed_value
    )
    return response
