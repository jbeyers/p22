"""Setup tests for this package."""
from p22.testing import P22_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that p22 is properly installed."""

    layer = P22_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if p22 is installed."""
        self.assertTrue(self.installer.is_product_installed("p22"))

    def test_browserlayer(self):
        """Test that IP22Layer is registered."""
        from p22.interfaces import IP22Layer
        from plone.browserlayer import utils

        self.assertIn(IP22Layer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("p22:default")[0],
            "20230226001",
        )


class TestUninstall(unittest.TestCase):

    layer = P22_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("p22")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if p22 is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("p22"))

    def test_browserlayer_removed(self):
        """Test that IP22Layer is removed."""
        from p22.interfaces import IP22Layer
        from plone.browserlayer import utils

        self.assertNotIn(IP22Layer, utils.registered_layers())
