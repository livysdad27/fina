#!/usr/bin/python
import os, pandas

def updateCat(payeeName, catName, dFrame):
  '''Update a category and re-persist the DataFrame to pickle again'''
  dFrame.loc[dFrame['payee'] == payeeName, 'cat'] = catName
  dFrame.to_pickle(os.path.join("data", "master.pkl"))
