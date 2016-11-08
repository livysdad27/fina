#!/usr/bin/python
from finaLib import finaImp 
from finaLib import finaExp
import unittest, os, pandas, shutil

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    pass
 
  def tearDown(self):
    pass

  def testDataDirExists(self):
    '''******Test that the data directory exists'''
    self.assertTrue(os.path.exists("data"))

  def testImportCSV(self):
    '''******Test a good file and make sure importOFX returns a pandas DataFrame object '''
    self.assertIsInstance(finaImp.importOFX(open("tests/assets/test.OFX")), pandas.core.frame.DataFrame)

  def testPickleDataFrame(self):
    '''******Test that we can pickle a data frame successfully.'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    finaImp.pickleDataFrame(df, "this.pkl", "tests/assets")
    self.assertTrue(os.path.isfile("tests/assets/this.pkl"))
    os.remove("tests/assets/this.pkl") 
