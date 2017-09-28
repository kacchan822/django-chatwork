from django.test import TestCase, override_settings

from chatwork.backends import DummyBackend, UrllibBackend, get_backend


class DummyBackendTests(TestCase):
    def test_return_empty(self):
        backend = DummyBackend()
        self.assertEqual(backend.get('/me'), {})

class GetBackendTests(TestCase):
    def test_default_backend(self):
        with override_settings(DEBUG=True):
            self.assertEqual(get_backend(), DummyBackend)
        with override_settings(DEBUG=False):
            self.assertEqual(get_backend(), UrllibBackend)
