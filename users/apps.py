from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

def __str__(self):
    return f"Профиль {self.user.username}"