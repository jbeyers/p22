"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "p22"

_ = MessageFactory("p22")

logger = logging.getLogger("p22")
