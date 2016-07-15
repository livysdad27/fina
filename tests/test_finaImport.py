#!/usr/bin/python
from finaImport import finaImport 
import unittest, os, pandas

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    finaImport.importCSV("testopesto")
    toeFile = open(os.path.join("data", "toe"), "w+")
    toeFile.write('hi, bye')
    toeFile.write('1,2')
    toeFile.write('3,4')

    emptyFile = open(os.path.join("data", "empty"), "w+")
 
  def tearDown(self):
    os.remove(os.path.join("data", "toe"))
    os.remove(os.path.join("data", "empty"))

  def testDataDirExists(self):
    '''Test that the data directory exists'''
    self.assertTrue(os.path.exists("data"))

  def testImportCSV(self):
    ''' Test a good file and make sure importCSV returns a csv reader object '''
    self.assertIsInstance(finaImport.importCSV("toe"), pandas.core.frame.DataFrame)

  def testImportBadFile(self):
    ''' Test a non-existant file '''
    self.assertEquals(finaImport.importCSV("testopesto"), "File not found!")

  def testImportEmptyFile(self):
    '''Test an empty file import'''
    self.assertEquals(finaImport.importCSV("empty"), "Bad csv file!")
