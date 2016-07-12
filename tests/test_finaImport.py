#!/usr/bin/python
from finaImport import finaImport 
import unittest
import os

class testImport(unittest.TestCase):
  '''Tests for importing a CSV file'''

  def setUp(self):
    toeFile = open(os.path.join("data", "toe"), "w+")
 
  def tearDown(self):
    os.remove(os.path.join("data", "toe"))

  def testImportCSV(self):
    ''' Test a good file '''
    self.assertIsInstance(finaImport.importCSV("toe") , file)

  def testImportBadFile(self):
    ''' Test a non-existant file '''
    self.assertEquals(finaImport.importCSV("Buttface"), "File not found!")
