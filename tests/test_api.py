import unittest

from unittest import mock
from invoca.api import Invoca
from invoca.enumerations import AccountType
from invoca.exceptions import InvocaException, UnsupportedApiVersionError


def mocked_transaction(*args, **kwargs):
    class MockResponse():
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse([{
        'advertiser_name': '',
        'advertiser_id': '',
        'affiliate_name': '',
        'affiliate_id': ''
    }], 200)


class TestAPIRequest(unittest.TestCase):

    def setUp(self):
        self.oauth_token = 'AifDHFUhFU@*f723f'
        self.n_name = 'boldmediagroup'
        self.n_id = 10
        self.version_date = '2017-04-01'
        self.api = Invoca(
            oauth_token=self.oauth_token,
            network_name=self.n_name,
            network_id=self.n_id,
            api_version=self.version_date
        )

    def test_accepts_correct_parameters(self):
        self.assertEqual(self.oauth_token, self.api.oauth_token)
        self.assertEqual(self.n_name, self.api.network_name)
        self.assertEqual(self.n_id, self.api.network_id)
        self.assertEqual(self.version_date, self.api.api_version)

    def test_raises_exception_on_unsupported_api_version(self):
        version_date = '0000-00-00'
        with self.assertRaises(UnsupportedApiVersionError):
            Invoca(
                oauth_token='',
                network_name='',
                network_id=0,
                api_version=version_date
            )

    def test_base_api_url_generates_based_on_network_values_supplied(self):
        expected_url = 'https://boldmediagroup.invoca.net/api/2017-04-01'
        self.assertEqual(expected_url, self.api.url)

    def test_url_builder_appends_path_to_url(self):
        o_url = self.api.url_builder('/advertisers/transactions')
        expected_url = ('https://boldmediagroup.invoca.net'
                        '/api/2017-04-01/advertisers/transactions')

        self.assertEqual(o_url, expected_url)

    def test_url_builder_removes_trailing_slash(self):
        o_url = self.api.url_builder('/test/path/')
        expected_url = ('https://boldmediagroup.invoca.net'
                        '/api/2017-04-01/test/path')

        self.assertEqual(o_url, expected_url)

    def test_url_builder_appends_resource_after_path(self):
        o_url = self.api.url_builder('/test/path/', resource=33)
        expected_url = ('https://boldmediagroup.invoca.net'
                        '/api/2017-04-01/test/path/33.json')

        self.assertEqual(o_url, expected_url)

    @mock.patch('invoca.api.requests.get', side_effect=mocked_transaction)
    def test_send_request_accepts_url(self, mocked_func):
        url = 'https://google.com'
        self.api._request(url)

    @mock.patch('invoca.api.requests.get', side_effect=mocked_transaction)
    def test_request_merges_oauth_token_and_filters(self, mocked_func):
        url = 'https://google.com'
        filters = {'filter-key': 'filter-val'}
        self.api._request(url, **filters)

        expected_request_params = {
            'oauth_token': self.oauth_token,
            'filter-key': 'filter-val'
        }
        mocked_func.assert_called_with(url, params=expected_request_params)

    def test_transactions_account_type_param_can_only_be_enum(self):
        with self.assertRaises(InvocaException):
            self.api.transactions(account_type='transaction')

    def test_transactions_requires_resource_id_if_not_network_account(self):
        with self.assertRaises(InvocaException):
            self.api.transactions(account_type=AccountType.PUBLISHER)

    @mock.patch('invoca.api.requests.get', side_effect=mocked_transaction)
    def test_transactions_allows_resource_id_override(self, mocked_func):
        self.api.transactions(
            account_type=AccountType.PUBLISHER, account_id=20)

        self.assertTrue(mocked_func.called)

    @mock.patch('invoca.api.requests.get', side_effect=mocked_transaction)
    def test_transactions_returns_list_of_dicts(self, mocked_func):
        transactions = self.api.transactions(AccountType.PUBLISHER, 20)

        self.assertTrue(isinstance(transactions, list))
        self.assertTrue(isinstance(transactions[0], dict))
