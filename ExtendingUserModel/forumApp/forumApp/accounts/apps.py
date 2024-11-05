from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forumApp.accounts'

    def ready(self):
        import forumApp.accounts.signals