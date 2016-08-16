# -*- coding: utf-8 -*-
import cherrypy, unittest

from fina import fina
from finaLib import cptestcase as ctc 

def setUpModule():
    cherrypy.tree.mount(fina(), '/', "fina.cfg")
    cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule

class TestCherryPyApp(ctc.BaseCherryPyTestCase):
    def test_get(self):
        response = self.request('/?thing=doh')
        self.assertEqual(response.output_status, '200 OK')
        # response body is wrapped into a list internally by CherryPy
        #self.assertEqual(response.body, ['this is a get request'])


