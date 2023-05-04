from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CS295P_Project'


class AccountConfig(AppConfig):
    name = 'CS295P_Project'
    def ready(self):
        import views.notice
