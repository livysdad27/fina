#!/usr/bin/python
import os, pandas
from datetime import datetime as dt

def unPickleDataFrame(pklFile="master.pkl"):
  '''Unpickle a dataframe so we can do things to it.  Use master.pkl as the default'''
  fullPklFileName=os.path.join("data", pklFile)
  if not(os.path.isfile(fullPklFileName)):
    return "Couldn't find file!"
  else:
    return pandas.read_pickle(fullPklFileName)     

def updateCat(payeeName, catName, pklFile="master.pkl"):
  '''Update a category and re-persist the DataFrame to pickle again'''
  fullFileName = os.path.join("data", pklFile)
  backupFileName = pklFile + str(dt.now()).replace(' ','')
  dFrame = pandas.read_pickle(fullFileName)
  dFrame.loc[dFrame['payee'] == payeeName, 'cat'] = catName
  os.rename(os.path.join("data", pklFile), os.path.join("data", backupFileName))
  dFrame.to_pickle(fullFileName)
