import cherrypy, unittest, os, shutil

from finaLib import finaDisp as fd
from fina import fina
from . import cptestcase as ctc 

def setUpModule():
  shutil.copy("tests/assets/test.pkl", "data") 
  cherrypy.tree.mount(fina(), '/', "fina.cfg")
  cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
  os.remove(os.path.join("data", "test.pkl"))
  cherrypy.engine.exit()
teardown_module = tearDownModule

class TestCherryPyApp(ctc.BaseCherryPyTestCase):
  '''Test class for the main cherry.py dispatcher.'''
  def test_get(self):
    '''******Test a get request using a test pkl file'''            
    response = self.request('/')
    self.assertEqual(response.output_status, '200 OK')
