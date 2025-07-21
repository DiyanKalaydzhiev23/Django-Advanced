from django.urls import path

from forumApp.common.views import view_counter, SetTimeCookie, notify_all_users

urlpatterns = [
    path('count/', view_counter, name='count'),
    path('last-visit/', SetTimeCookie.as_view(), name='set-time'),
    path('notify/', notify_all_users, name='notify'),
]