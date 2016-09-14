#!/usr/bin/python
import os, pandas

def updateCat(payeeName, catName, dFrame):
  '''Update a category and re-persist the DataFrame to pickle again'''
  dFrame.loc[dFrame['payee'] == payeeName, 'cat'] = catName
  os.rename(os.path.join("data", pklFile), os.path.join("data", backupFileName))
  dFrame.to_pickle(fullFileName)
