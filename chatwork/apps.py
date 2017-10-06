from django.apps import AppConfig
from django.conf import settings


class ChatworkConfig(AppConfig):
    name = 'chatwork'

    DEFAULT_BACKEND = 'chatwork.backends.dummy.DummyBackend' \
        if settings.DEBUG else 'chatwork.backends.http.UrllibBackend'
    BACKEND = getattr(settings, 'CHATWORK_API_BACKEND', DEFAULT_BACKEND)
