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

  def testDispOFX(self):
    '''******Test that we can do the basic return of a DF and it's HTML'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    odf, ostr = finaDisp.dispOFX(df)
    self.assertIsInstance(odf, pandas.core.frame.DataFrame)
    self.assertIsInstance(ostr, basestring)

  def testDispDFrameByDate(self):
    '''******Test that we can do a return of the DF and it's HTML by date'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    odf, ostr = finaDisp.dispDFrameByDate('2016-01-01 00:00:00', '2016-02-02 00:00:00', df)
    self.assertIsInstance(odf, pandas.core.frame.DataFrame)
    self.assertIsInstance(ostr, basestring)
 
  def testDispDFrameByCat(self):
    '''******Test that we can do a return of the DF and it's HTML by cat'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    odf, ostr = finaDisp.dispDFrameByCat('hoser' , df)
    self.assertIsInstance(odf, pandas.core.frame.DataFrame)
    self.assertIsInstance(ostr, basestring)

  def testDispPareto(self):
    '''******Test that we can spit out a buffered chart'''
    df = finaExp.unPickleData("test.pkl", "tests/assets")
    buf = finaDisp.dispPareto(df)
    self.assertIsInstance(buf, cStringIO.OutputType)

#  def testDispMonthPareto(self):
#    '''******Test that we can spit out a buffered chart for a month pareto'''
#    df = finaExp.unPickleData("test.pkl", "tests/assets")
#    buf = finaDisp.dispMonthPareto(df, '')
#    self.assertIsInstance(buf, cStringIO.OutputType)
