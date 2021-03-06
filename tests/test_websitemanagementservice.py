# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------

from azure.servicemanagement.websitemanagementservice import (
    WebsiteManagementService,
    )

from azure.servicemanagement import (
    WebSpaces,
    WebSpace,
    Sites,
    Site,
    )

from .util import (
    AzureTestCase,
    credentials,
    set_service_options,
    )
import unittest

class WebSiteServiceTest(AzureTestCase):

    def setUp(self):
        self.wss = WebsiteManagementService(credentials.getSubscriptionId(),
                                            credentials.getManagementCertFile())
        set_service_options(self.wss)

    def tearDown(self):
        self.cleanup()
        return super(WebSiteServiceTest, self).tearDown()

    def cleanup(self):
        pass # No clean needed by now
    
    def test_list_web_spaces(self):
        result = self.wss.list_webspaces()
        
        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, WebSpaces)
        
        self.assertTrue(len(result) > 0)
        
        webspace = None
        for temp in result:
            # I need lower()?
            if temp.name.lower() == 'eastuswebspace':
                webspace = temp
                break
        self.assertEqual(webspace.geo_location, 'BLU')
        self.assertEqual(webspace.geo_region, 'East US')

    def test_get_web_space(self):
        result = self.wss.get_webspace('eastuswebspace')
        
        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, WebSpace)
        
        self.assertEqual(result.geo_location, 'BLU')
        self.assertEqual(result.geo_region, 'East US')

    @unittest.skip
    def test_list_web_sites(self):
        result = self.wss.list_sites('eastuswebspace')
        
        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Sites)
        
        self.assertTrue(len(result) > 0)
        
    @unittest.skip
    def test_get_web_site(self):
        result = self.wss.get_site('eastuswebspace',
                                   'mywebsite')
        
        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Site)
        
        self.assertTrue(len(result) > 0)
