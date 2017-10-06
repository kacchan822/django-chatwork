import datetime
import json
import urllib.request
from urllib.error import HTTPError

from django.utils.http import urlencode

from .base import BaseBackend
from ..exceptions import EXCEPTION_LABEL


class UrllibBackend(BaseBackend):
    def request(self, endpoint, method, data=None):
        data_encoded = self.__encode_data(data) if data else None
        request = urllib.request.Request(
            self.endpoint_base + endpoint,
            data=data_encoded,
            headers=self.request_header,
            method=method
        )
        try:
            response = urllib.request.urlopen(request)
        except HTTPError as error:
            response = error
        return self.__validate(response)

    def __update_rate_limit(self, response):
        self.rate_limit = getattr(response.headers, 'X-RateLimit-Limit', 100)
        self.rate_limit_remaining = getattr(
            response.headers, 'X-RateLimit-Remaining', 100)
        self.rate_limit_reset = datetime.datetime.fromtimestamp(
            int(getattr(response.headers, 'X-RateLimit-Reset', 0))).isoformat()

    def __validate(self, response):
        self.__update_rate_limit(response)
        if response.headers['Content-Type'].startswith('application/json'):
            result = json.loads(response.read().decode('utf-8'))
            return result
        elif not self.fail_silently:
            raise EXCEPTION_LABEL['invalid_response']
        else:
            return {'errors': ['Invalid Response']}

    def __encode_data(self, data):
        return urlencode(data).encode('utf-8') if data else None
