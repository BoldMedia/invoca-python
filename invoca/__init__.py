import logging

from .api import Invoca
from .exceptions import InvocaException, UnsupportedApiVersionError

__version__ = '1.0.1'

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
