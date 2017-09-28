"""
Dummy backend that does nothing.
"""
import sys

from django.utils.text import force_text

from .base import BaseBackend


class DummyBackend(BaseBackend):
    def request(self, endpoint, method, data=None):
        request = '{}\nmethod: {}\nendpoint: {}\ndata: {}\n{}\n'.format(
            '-' * 79,
            method,
            self.endpoint_base + endpoint,
            force_text(data),
            '-' * 79
        )
        sys.stdout.write(request)
        return {}
