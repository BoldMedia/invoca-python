
class InvocaException(Exception):
    pass


class UnsupportedApiVersionError(InvocaException):
    pass


class InvalidAccountTypeError(InvocaException):
    pass
