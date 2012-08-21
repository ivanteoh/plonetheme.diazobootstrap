from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig


class DiazoBootstrap(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonetheme.diazobootstrap
        xmlconfig.file('configure.zcml', plonetheme.diazobootstrap, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.diazobootstrap:default')

DIAZO_BOOTSTRAP_FIXTURE = DiazoBootstrap()
DIAZO_BOOTSTRAP_INTEGRATION_TESTING = IntegrationTesting(bases=(DIAZO_BOOTSTRAP_FIXTURE,), name="DiazoBootstrap:Integration")
DIAZO_BOOTSTRAP_FUNCTIONAL_TESTING = FunctionalTesting(bases=(DIAZO_BOOTSTRAP_FIXTURE,), name="DiazoBootstrap:Functional")
