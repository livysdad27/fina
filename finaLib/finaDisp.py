#!/usr/bin/python
import os, pandas

pandas.set_option('display.max_colwidth', -1)

def dispOFX(dFrame):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    dFrameHTML = dFrame.to_html(escape=False)
    return dFrame, dFrameHTML
  except(IOError):
    return "File not found!"

def dispDFrameByDate(startDate, endDate, dFrame): 
  '''dispDFrameByDate slices a date range out of a dataframe'''
  sDate = pandas.to_datetime(startDate)
  eDate = pandas.to_datetime(endDate)
  if (pandas.isnull(sDate) or pandas.isnull(eDate)):
    dFrameHTML = dFrame.to_html(escape=False)
    return dFrame, dFrameHTML  
  else:
    sliceDFrame = dFrame.loc[(dFrame['date'] > sDate) & (dFrame['date'] < eDate)]
    sliceDFrameHTML = sliceDFrame.to_html(escape=False)
    return sliceDFrame, sliceDFrameHTML

def dispDFrameByCat(cat, dFrame):
  '''Display the items with a given category'''
  sliceDFrame = dFrame.loc[dFrame['cat'] == cat]
  sliceDFrameHTML = sliceDFrame.to_html(escape=False, columns=('payee', 'amount', 'date'))
  return sliceDFrame, sliceDFrameHTML

def dispDFrameByMonth(yearNum, monthNum, dFrame):
  '''dispDFrameByMonth slices a month of transactions out of the dataframe'''
  sliceDFrame = dFrame.loc[(dFrame['date'].month == monthNum) & (dFrame['date'].year == yearNum)]
  sliceDFrameHTML = sliceDFrame.to_html()
  return sliceDFrame, sliceDFrameHTML
