#!/usr/bin/python
from finaImport import finaImport 
import unittest, os, csv

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    finaImport.importCSV("testopesto")
    toeFile = open(os.path.join("data", "toe"), "w+")
 
  def tearDown(self):
    os.remove(os.path.join("data", "toe"))

  def testDataDirExists(self):
    '''Test that the data directory exists'''
    self.assertTrue(os.path.exists("data"))

  def testImportCSV(self):
    ''' Test a good file and make sure importCSV returns a csv reader object '''
    readerObject = finaImport.importCSV("toe")
    self.assertTrue(str(type(readerObject)), "_csv.reader")

  def testImportBadFile(self):
    ''' Test a non-existant file '''
    self.assertEquals(finaImport.importCSV("testopesto"), "File not found!")
