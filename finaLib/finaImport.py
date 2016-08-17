#!/usr/bin/python
import os, pandas
from ofxparse import OfxParser as ofp

def importOFX(fileName):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  try:
    transList = []
    fileFullName = os.path.join("data", fileName)
    ofx = ofp.parse(open(fileFullName))
    for t in ofx.account.statement.transactions:
      transList.append({'id':t.id, 'amount':t.amount, 'checknum':t.checknum, 'date':t.date, 'mcc':t.mcc, 'memo':t.memo, 'payee':t.payee, 'sic':t.sic, 'type':t.type})

    return pandas.DataFrame(transList)
  except(IOError):
    return "File not found!"
  except:
    return "Bad ofx file!"

def pickleDataFrame(ofxDataFrame):
  '''Write out a the master pickled dataframe.'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  pickleFullName = os.path.join("data", "master.pkl") 
  ofxDataFrame.to_pickle(pickleFullName)
