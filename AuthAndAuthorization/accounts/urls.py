from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from accounts import views
from accounts.views import set_unusable_password_view

urlpatterns = [
    path('fbv/login/', views.login_fbv, name='fbv-login'),
    path('fbv/logout/', views.logout_fbv, name='fbv-logout'),
    path('fbv/register/', views.register_fbv, name='fbv-register'),
    path('cbv/login/', LoginView.as_view(), name='cbv-login'),
    path('cbv/logout/', LogoutView.as_view(), name='cbv-logout'),
    path('set-unusable-password/', set_unusable_password_view, name='set-unusable-password'),

    # Change of password when we know it
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Forgotten password
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirmed'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
