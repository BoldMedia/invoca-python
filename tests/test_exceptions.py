import unittest
import invoca.exceptions as exceptions


class TestExceptions(unittest.TestCase):

    def test_exceptions_all_inherit_base_exception(self):
        unsupported_api_version = exceptions.UnsupportedApiVersionError()
        invalid_account_type = exceptions.InvalidAccountTypeError()

        self.assertIsInstance(
            unsupported_api_version, exceptions.InvocaException)

        self.assertIsInstance(
            invalid_account_type, exceptions.InvocaException)
