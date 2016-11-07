#!/usr/bin/python
from finaLib import finaImp 
import unittest, os, pandas, shutil

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    shutil.copy("tests/assets/test.OFX", "data")
    toeFile = open(os.path.join("data", "test.OFX"))
    badFile = open(os.path.join("data", "bad.OFX"), "w+")
    badFile.write("A,B,C")
    emptyFile = open(os.path.join("data", "empty.OFX"), "w+")
 
  def tearDown(self):
    os.remove(os.path.join("data", "test.OFX"))
    os.remove(os.path.join("data", "empty.OFX"))
    os.remove(os.path.join("data", "bad.OFX"))

  def testDataDirExists(self):
    '''******Test that the data directory exists'''
    self.assertTrue(os.path.exists("data"))

  def testImportCSV(self):
    '''******Test a good file and make sure importOFX returns a pandas DataFrame object '''
    self.assertIsInstance(finaImp.importOFX(open("data/test.OFX")), pandas.core.frame.DataFrame)
