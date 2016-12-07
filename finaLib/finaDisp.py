#!/usr/bin/python
import os, pandas, matplotlib, urllib
from cStringIO import StringIO as sio
from matplotlib import rcParams

matplotlib.use('Agg')
pandas.set_option('display.max_colwidth', -1)
rcParams.update({'figure.autolayout': True})

def dispOFX(dFrame):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    dFrameHTML = dFrame.to_html(escape=False, classes="transTable table-condensed")
    return dFrame, dFrameHTML
  except(IOError):
    return "File not found!"

def dispDFrameByDate(startDate, endDate, dFrame): 
  '''dispDFrameByDate slices a date range out of a dataframe'''
  sDate = pandas.to_datetime(startDate)
  eDate = pandas.to_datetime(endDate)
  if (pandas.isnull(sDate) or pandas.isnull(eDate)):
    dFrameHTML = dFrame.to_html(escape=False, classes="transTable table-condensed")
    return dFrame, dFrameHTML  
  else:
    sliceDFrame = dFrame.loc[(dFrame['date'] > sDate) & (dFrame['date'] < eDate)]
    sliceDFrameHTML = sliceDFrame.to_html(escape=False, classes="transTable table-condensed")
    return sliceDFrame, sliceDFrameHTML

def dispDFrameByCat(cat, dFrame):
  '''Display the items with a given category'''
  sliceDFrame = dFrame.loc[dFrame['cat'] == cat]
  sliceDFrameHTML = sliceDFrame.to_html(escape=False, classes='payeeTable table-condensed')
  if len(sliceDFrame.index) == 0:
    sliceDFrameHTML = ''
  return sliceDFrame, sliceDFrameHTML

def dispDFrameById(tid, dFrame):
  '''Display the item with a given tid'''
  tid = urllib.unquote(tid).decode()
  df = dFrame.loc[dFrame['id'] == tid]
  transId = str(df.iloc[0]['id'])
  transAmount = str(df.iloc[0]['amount'])
  transPayee = df.iloc[0]['payee']
  transCat = df.iloc[0]['cat']
  transDate = str(df.iloc[0]['date'])
  transDeets = "<b>Payee:</b> " + transPayee + "<br> <b>Date:</b> " + transDate + "<br> <b>Amount:</b> " + transAmount + "<br> <b>Cat:</b> " + transCat + "<input type='hidden' class='overrideTid' name='tid' value='" + transId + "'></input>"
  return transDeets 

def dispPareto(dFrame):
  dFrame.amount = dFrame.amount.astype('float')
  dFrame = dFrame.groupby('cat').sum().sort_values('amount')
  plot = dFrame.plot.bar(color='grey')
  fig = plot.get_figure()
  buf = sio()
  fig.savefig(buf, format='png')
  return buf 

def dispMonthPareto(dFrame, cat):
  dFrame.amount = dFrame.amount.astype('float')
  dFrame = dFrame.loc[dFrame['cat']==cat]
  dFrame = dFrame.groupby([ dFrame['date'].dt.month, dFrame['date'].dt.year ]).sum().sort_values('amount')
  plot = dFrame.plot.bar(color='grey')
  fig = plot.get_figure()
  buf = sio()
  fig.savefig(buf, format='png')
  return buf 
