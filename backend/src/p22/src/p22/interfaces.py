"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IP22Layer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
