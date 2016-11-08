#!/usr/bin/python
import finaExp as fe
import os, pandas
from ofxparse import OfxParser as ofp 
from ofxparse.ofxparse import OfxParserException as ofpe

def importOFX(fileName):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  if not(os.path.exists("data")):
      os.makedirs("data")
  currentData = fe.unPickleData()
  transList = [] 
  ofx = ofp.parse(fileName)
  for t in ofx.account.statement.transactions:
    transList.append({'id':t.id, 'amount':t.amount, 'checknum':t.checknum, 'date':t.date, 'mcc':t.mcc, 'memo':t.memo, 'payee':t.payee, 'sic':t.sic, 'type':t.type, 'cat':''})

  df = pandas.DataFrame.from_records(transList)
  df.amount = df.amount.astype(float)
  df = pandas.concat([df, currentData]).drop_duplicates(subset='id', keep='last')
  return df

def pickleDataFrame(ofxDataFrame, pklFile="master.pkl", pklDir="data"):
  '''Write out a the master pickled dataframe.'''
  if not(os.path.exists(pklDir)):
    os.makedirs(pklDir)
  pickleFullName = os.path.join(pklDir, pklFile) 
  ofxDataFrame.to_pickle(pickleFullName)
