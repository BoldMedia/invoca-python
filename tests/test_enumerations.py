import unittest

from invoca.enumerations import ResponseStatus, AccountType, TransactionType


class TestResponseStatus(unittest.TestCase):

    def test_status_codes_correctly_map(self):
        self.assertEqual(ResponseStatus.OK, 200)
        self.assertEqual(ResponseStatus.CREATED, 201)
        self.assertEqual(ResponseStatus.UNAUTHORIZED, 401)
        self.assertEqual(ResponseStatus.FORBIDDEN, 403)
        self.assertEqual(ResponseStatus.NOT_FOUND, 404)
        self.assertEqual(ResponseStatus.INTERNAL_SERVER_ERROR, 500)


class TestAccountType(unittest.TestCase):

    def test_values_are_correctly_mapped(self):
        self.assertEqual(AccountType.PUBLISHER.value, 'publisher')
        self.assertEqual(AccountType.ADVERTISER.value, 'advertiser')
        self.assertEqual(AccountType.NETWORK.value, 'network')

    def test_plural_returns_correct_values(self):
        self.assertEqual(AccountType.PUBLISHER.plural, 'publishers')
        self.assertEqual(AccountType.ADVERTISER.plural, 'advertisers')
        self.assertEqual(AccountType.NETWORK.plural, 'networks')


class TestTransactionType(unittest.TestCase):

    def test_values_are_correctly_mapped(self):
        self.assertEqual(TransactionType.CALL.value, 'call')
        self.assertEqual(TransactionType.SALE.value, 'sale')
        self.assertEqual(TransactionType.SIGNAL.value, 'signal')
