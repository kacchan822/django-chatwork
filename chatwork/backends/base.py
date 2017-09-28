import sys

from django.conf import settings

from ..exceptions import EXCEPTION_LABEL


class BaseBackend:
    def __init__(self, **kwargs):
        endpoint_base = getattr(settings, 'CHATWORK_API_ENDPOINT_BASE',
                                'https://api.chatwork.com/v2')
        api_token = getattr(settings, 'CHATWORK_API_TOKEN', '')
        self.endpoint_base = kwargs.get('endpoint_base') or endpoint_base
        self.api_token = kwargs.get('api_token') or api_token
        self.request_header = {'X-ChatWorkToken': self.api_token}
        self.rate_limit = None
        self.rate_limit_remaining = None
        self.rate_limit_reset = None
        self.fail_silently = getattr(settings, 'CHATWORK_API_FAIL_SILENTLY',
                                     False)

        if not self.api_token:
            if settings.DEBUG:
                sys.stdout.write('Warning: CHATWORK_API_TOKEN is missing!\n')
            else:
                raise EXCEPTION_LABEL['no_auth_token']

    def request(self, endpoint, method, data=None):
        raise NotImplementedError('subclasses of BaseBackend must override'
                                  ' request() method')

    def get(self, endpoint, data=None):
        return self.request(endpoint, method='GET', data=data)

    def post(self, endpoint, data=None):
        return self.request(endpoint, method='POST', data=data)

    def put(self, endpoint, data=None):
        return self.request(endpoint, method='PUT', data=data)

    def delete(self, endpoint, data=None):
        return self.request(endpoint, method='DELETE', data=data)
