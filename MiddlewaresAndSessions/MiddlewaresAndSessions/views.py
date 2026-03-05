from datetime import timezone, timedelta
from django.core.signing import Signer, BadSignature
from django.conf import settings
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.utils.timezone import now


def choose_language(request):
    if request.method == "POST":
        selected_language = request.POST.get('language', '').lower()

        if selected_language in settings.SUPPORTED_LANGUAGES:
            request.session['language'] = selected_language

        return redirect('home')  # TODO fix the url

    current_language = request.session.get('language', 'en')

    return render(
        request,
        'choose_language.html',
        {
            'current_language': current_language,
            'supported_languages': settings.SUPPORTED_LANGUAGES,
        }
    )


def home_page(request):
    GREETING_MESSAGES = {
        "en": "Hello! How are you today?",
        "de": "Hallo! Wie geht es Ihnen heute?",
        "bg": "Здравей! Как си днес?",
    }

    current_language = request.session.get('language', 'en')
    greeting_message = GREETING_MESSAGES[current_language]

    return render(
        request,
        'home_page.html',
        {
            "current_language": current_language,
            "greeting_message": greeting_message
        }
    )


def session_expiry(request):
    error_message = ''

    if request.method == "POST":
        expiry_value = request.POST.get('expiry_seconds', 0)

        try:
            expiry_seconds = int(expiry_value)
            if expiry_seconds <= 0:
                raise ValueError
        except ValueError:
            error_message = 'Enter a positive number of seconds.'
        else:
            request.session.set_expiry(expiry_seconds)
            return redirect('session-expiry')

    return render(
        request,
        'session_expiry.html',
        {
            'remaining_seconds': request.session.get_expiry_age(),
            'error_message': error_message,
        }
    )


def clear_session(request):
    request.session.pop('language')
    return redirect('home')


def flush_session(request):
    request.session.flush()
    return redirect('home')


def read_theme_cookie(request):
    return render(
        request,
        'read_theme_cookie.html',
        {
            'theme_value': request.COOKIES.get('theme'),
        }
    )


def set_theme_cookie(request):
    response = redirect('read-theme-cookie')
    response.set_cookie(
        key='theme',
        value='dark',
        expires=now() + timedelta(hours=1),
        secure=True,  # send this only over https
        httponly=True,  # JS can't access the cookie
    )
    return response


def read_signed_cookie(request):
    role_cookie = request.COOKIES.get('role', '')
    signature_valid = False
    signer = Signer()

    try:
        verified_value = signer.unsign(role_cookie)
        signature_valid = True
    except BadSignature:
        verified_value = 'Invalid signature'


    return render(
        request,
        'read_signed_cookie.html',
        {
            'signature_valid': signature_valid,
            'verified_value': verified_value,
        }
    )


def set_signed_cookie(request):
    signer = Signer()
    # user:wuihofibry378r7347fg
    signed_value = signer.sign('user')  # SECRET_KEY + 'user' HMAC sha256 -> hash
    response = redirect('read-signed-cookie')
    response.set_cookie(
        key='role',
        value=signed_value,
    )
    return response
