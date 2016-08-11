#!/usr/bin/python
from finaLib import finaImport 
import unittest, os, pandas, shutil

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    shutil.copy("tests/assets/test.OFX", "data")
    
    toeFile = open(os.path.join("data", "test.OFX"))
    emptyFile = open(os.path.join("data", "emptyofx"), "w+")
 
  def tearDown(self):
    os.remove(os.path.join("data", "test.OFX"))
    os.remove(os.path.join("data", "emptyofx"))

  def testDataDirExists(self):
    '''Test that the data directory exists'''
    self.assertTrue(os.path.exists("data"))

  def testImportCSV(self):
    ''' Test a good file and make sure importCSV returns a csv reader object '''
    self.assertIsInstance(finaImport.importOFX("test.OFX"), pandas.core.frame.DataFrame)

  def testImportBadFile(self):
    ''' Test a non-existant file '''
    self.assertEquals(finaImport.importOFX("testopesto"), "File not found!")

  def testImportEmptyFile(self):
    '''Test an empty file import'''
    self.assertEquals(finaImport.importOFX("empty"), "Bad ofx file!")
