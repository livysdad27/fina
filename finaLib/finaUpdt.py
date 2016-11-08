#!/usr/bin/python
import finaImp as fi
import os, pandas

def updateCat(payeeName, catName, dFrame, dirName="data", pklName="master.pkl"):
  '''Update a category and re-persist the DataFrame to pickle again'''
  dFrame.loc[dFrame['payee'] == payeeName, 'cat'] = catName
  fi.pickleDataFrame(dFrame, pklName, dirName)
  return True
