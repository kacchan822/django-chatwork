"""
Dummy backend that does nothing.
"""
import json
import re

from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import render_to_string

from .base import BaseBackend


def replace_id(endpoint):
    if endpoint.startswith('/rooms'):
        repl = 'room_id'
    elif endpoint.startswith('/incoming_requests'):
        repl = 'request_id'
    else:
        return endpoint
    return re.sub(r'[0-9]+', repl, endpoint)


class DummyBackend(BaseBackend):
    def request(self, endpoint, method, data=None):
        context = {
            'endpoint': endpoint,
            'method': method.upper(),
        }
        if data:
            context.update(data)

        endpoint = replace_id(endpoint)

        if method.upper() == 'GET':
            template_name = 'chatwork/dummy{}.json'.format(endpoint)
        else:
            template_name = 'chatwork/dummy{}_{}.json'.format(endpoint,
                                                              method.upper())
        try:
            response = render_to_string(template_name, context)
        except TemplateDoesNotExist:
            response = '{}'

        return json.loads(response)
