from enum import Enum, IntEnum


class AccountType(Enum):
    PUBLISHER = 'publisher'
    NETWORK = 'network'
    ADVERTISER = 'advertiser'

    @property
    def plural(self):
        return '{}s'.format(self.value)


class ResponseStatus(IntEnum):
    OK = 200
    CREATED = 201
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class TransactionType(Enum):
    CALL = 'call'
    SALE = 'sale'
    SIGNAL = 'signal'
