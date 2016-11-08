#!/usr/bin/python
from finaLib import finaDisp
from finaLib import finaImp 
from finaLib import finaExp
import unittest, os, pandas, shutil, cStringIO

class testImport(unittest.TestCase):
  '''Tests for importing a Displaying data''' 

  def setUp(self):
    pass
 
  def tearDown(self):
    pass

  def testUnPickleData(self):
    '''******Test both options for unpickling the dataframe'''
    self.assertIsInstance(finaExp.unPickleData("test.pkl", "tests/assets"), pandas.core.frame.DataFrame)
    self.assertIsInstance(finaExp.unPickleData("toejamb", "tests/assets"), pandas.core.frame.DataFrame)
