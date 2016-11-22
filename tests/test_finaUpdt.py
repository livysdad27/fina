#!/usr/bin/python
from finaLib import finaDisp
from finaLib import finaImp 
from finaLib import finaExp
from finaLib import finaUpdt
import unittest, os, pandas, shutil, cStringIO

class testImport(unittest.TestCase):
  '''Tests for updating cats''' 

  def setUp(self):
    pass
 
  def tearDown(self):
    pass

  def testUpdateCat(self):
    '''******Test that we can update a cat'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    odf, ostr = finaDisp.dispOFX(df)
    self.assertTrue(finaUpdt.updateCat('toe', 'jamb', None,  odf, "tests/assets", "test.pkl"))

