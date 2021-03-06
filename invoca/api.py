import logging
import requests

from .enumerations import AccountType
from .exceptions import (InvocaException,
                         UnsupportedApiVersionError,
                         InvalidAccountTypeError)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

SUPPORTED_API_VERSIONS = ['2017-04-01', '2017-09-01', '2018-02-01']
DEFAULT_API_VERSION = SUPPORTED_API_VERSIONS[0]


class Invoca:

    def __init__(self, oauth_token, network_name,
                 network_id, api_version=DEFAULT_API_VERSION):
        if api_version not in SUPPORTED_API_VERSIONS:
            raise UnsupportedApiVersionError(
                'Unsupported API version {}'.format(api_version))

        self.oauth_token = oauth_token
        self.network_name = network_name
        self.network_id = network_id
        self.api_version = api_version

    @property
    def url(self):
        return 'https://{0}.invoca.net/api/{1}'.format(
            self.network_name, self.api_version)

    def url_builder(self, path, resource=None):
        url = '{}{}'.format(self.url, path)

        if url[-1] == '/':
            url = url[:-1]

        if resource is not None:
            url = '{}/{}.json'.format(url, resource)

        return url

    def _request(self, url, **kwargs):
        params = {'oauth_token': self.oauth_token}
        params.update(kwargs)
        response = requests.get(url, params=params)

        if response.status_code is not 200 and response.status_code is not 201:
            logger.warning('Non-200 Request. Response: {}'.format(
                response.text))
            return None

        return response.json()

    def transactions(self, account_type=AccountType.NETWORK,
                     account_id=None, filters={}):
        if not isinstance(account_type, AccountType):
            raise InvalidAccountTypeError(
                'Expected value of type AccountType. Received {}'.format(
                    account_type))

        if account_type is AccountType.NETWORK:
            account_id = self.network_id
        elif account_id is None:
            raise InvocaException(
                'Expected account_id of type int. Received {}'.format(
                    account_id))

        url = self.url_builder(
            '/{}/transactions'.format(account_type.plural), account_id)
        response = self._request(url, **filters)
        if response is None:
            return []

        return response
