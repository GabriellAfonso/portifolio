from django.apps import AppConfig


class WebchatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.webchat'

    def ready(self):
        import apps.webchat.signals
