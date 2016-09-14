#!/usr/bin/python
import os, pandas

def dispOFX(dFrame):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    dFrameHTML = dFrame.to_html()
    return dFrame, dFrameHTML
  except(IOError):
    return "File not found!"

def dispDFrameByDate(startDate, endDate, dFrame): 
  '''dispDFrameByDate slices a date range out of a dataframe'''
  sDate = pandas.to_datetime(startDate)
  eDate = pandas.to_datetime(endDate)
  sliceDFrame = dFrame.loc[(dFrame['date'] > sDate) & (dFrame['date'] < eDate)]
  sliceDFrameHTML = sliceDFrame.to_html()
  return sliceDFrame, sliceDFrameHTML

def dispDFrameByMonth(yearNum, monthNum, dFrame):
  '''dispDFrameByMonth slices a month of transactions out of the dataframe'''
  sliceDFrame = dFrame.loc[(dFrame['date'].month == monthNum) & (dFrame['date'].year == yearNum)]
  sliceDFrameHTML = sliceDFrame.to_html()
  return sliceDFrame, sliceDFrameHTML
