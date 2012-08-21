import unittest2 as unittest
#import transaction

from plonetheme.diazobootstrap.testing import DIAZO_BOOTSTRAP_INTEGRATION_TESTING
#from plonetheme.diazobootstrap.testing import CUEBASE_THEME_FUNCTIONAL_TESTING

#from plone.testing.z2 import Browser
#from plone.app.testing import SITE_OWNER_NAME
#from plone.app.testing import SITE_OWNER_PASSWORD

#from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

#from plone.registry.interfaces import IRegistry
#from plone.app.theming.interfaces import IThemeSettings


class TestSetup(unittest.TestCase):

    layer = DIAZO_BOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'plonetheme.cuebase'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
