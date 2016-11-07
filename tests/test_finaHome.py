import cherrypy, unittest, os, shutil

from finaLib import finaDisp as fd
from fina import home 
from . import cptestcase as ctc 

def setUpModule():
  cherrypy.tree.mount(home(), '/', "home.cfg")
  cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
  cherrypy.engine.exit()
teardown_module = tearDownModule

class TestIndex(ctc.BaseCherryPyTestCase):
  '''Test class for the main cherry.py dispatcher.'''
  def test_get(self):
    '''******Test a get request using'''            
    response = self.request('/index.html')
    self.assertEqual(response.output_status, '200 OK')

class TestFinaJS(ctc.BaseCherryPyTestCase):
  '''Test class for the main cherry.py dispatcher.'''
  def test_get(self):
    '''******Test a get request using'''            
    response = self.request('/fina.js')
    self.assertEqual(response.output_status, '200 OK')

class TestDropzoneJS(ctc.BaseCherryPyTestCase):
  '''Test class for the main cherry.py dispatcher.'''
  def test_get(self):
    '''******Test a get request using'''            
    response = self.request('/dropzone.js')
    self.assertEqual(response.output_status, '200 OK')
