from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import p22


class P22Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=p22)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "p22:default")
        applyProfile(portal, "p22:initial")


P22_FIXTURE = P22Layer()


P22_INTEGRATION_TESTING = IntegrationTesting(
    bases=(P22_FIXTURE,),
    name="P22Layer:IntegrationTesting",
)


P22_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(P22_FIXTURE, WSGI_SERVER_FIXTURE),
    name="P22Layer:FunctionalTesting",
)


P22ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        P22_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="P22Layer:AcceptanceTesting",
)
