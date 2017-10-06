from django.test import TestCase
from django.utils.module_loading import import_string

from chatwork.apps import ChatworkConfig
from chatwork.backends import get_backend
from chatwork.backends.dummy import DummyBackend
from chatwork.backends.http import UrllibBackend


class DummyBackendTests(TestCase):
    def test_return_empty(self):
        backend = DummyBackend()
        self.assertEqual(backend.get('/me'), {})

class GetBackendTests(TestCase):
    def test_default_backend(self):
        default_backend = import_string(ChatworkConfig.DEFAULT_BACKEND)
        self.assertEqual(get_backend(), default_backend)

    def test_override_backend_dummy(self):
        dummy_backend = get_backend('chatwork.backends.dummy.DummyBackend')
        self.assertEqual(dummy_backend, DummyBackend)

    def test_override_backend_http(self):
        http_backend = get_backend('chatwork.backends.http.UrllibBackend')
        self.assertEqual(http_backend, UrllibBackend)
