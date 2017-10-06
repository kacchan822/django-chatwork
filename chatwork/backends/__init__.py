from django.utils.module_loading import import_string

from ..apps import ChatworkConfig


def get_backend(backend=None):
    use_backend = backend or ChatworkConfig.BACKEND
    return import_string(use_backend)
