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
    self.assertIsInstance(finaImport.importOFX("test.OFX"), pandas.core.frame.DataFrame)

  def testImportBadFile(self):
    '''******Test a non-existant file '''
    self.assertEquals(finaImport.importOFX("testopesto"), "File not found!")

  def testImportEmptyFile(self):
    '''******Test an empty file import'''
    self.assertEquals(finaImport.importOFX("empty.OFX"), "Likely an empty file but an OfxParserException was raised!")

  def testImportBadFile(self):
    '''******Test an empty file import'''
    self.assertEquals(finaImp.importOFX("bad.OFX"), "Bad OFX File or other ValueError")
