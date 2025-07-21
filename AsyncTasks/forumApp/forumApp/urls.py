from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from forumApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forumApp.posts.urls')),
    path('accounts/', include('forumApp.accounts.urls')),
    path('common/', include('forumApp.common.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
