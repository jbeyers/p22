from p22 import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if p22 is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IP22Layer is registered."""
        from p22.interfaces import IP22Layer

        assert IP22Layer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240728001"
