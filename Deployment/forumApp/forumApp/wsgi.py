import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forumApp.settings')

application = get_wsgi_application()


"""

manage.py

1. One instance of the project
2. Hot reloading
3. Servers static files


gunicorn

1. Specify how many workers you want
2. No hot reloading, totally stable
3. Doesn't serve static files

"""