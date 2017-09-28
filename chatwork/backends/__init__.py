from django.conf import settings

from .dummy import DummyBackend
from .http import UrllibBackend


def get_backend(backend=None):
    backends = {
        'dummy': DummyBackend,
        'http': UrllibBackend,
    }
    default = 'dummy' if settings.DEBUG else 'http'
    if getattr(settings, 'CHATWORK_API_BACKEND', None):
        default = getattr(settings, 'CHATWORK_API_BACKEND', None)
    return backends.get(backend, backends[default])
