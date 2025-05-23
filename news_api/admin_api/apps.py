# в apps.py твоего приложения user_api или admin_api
from django.apps import AppConfig

class AdminApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_api'

    def ready(self):
        import admin_api.signals  # импортируем signals, чтобы зарегистрировать обработчики
