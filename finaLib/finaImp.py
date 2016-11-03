#!/usr/bin/python
import os, pandas
import urllib
from cStringIO import StringIO as sio
#import ofxparse 
from ofxparse import OfxParser as ofp 
from ofxparse.ofxparse import OfxParserException as ofpe

def importOFX(fileName):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  try:
    transList = [] 
#    fileFullName = os.path.join("data", fileName)
#    buf = sio()
#    buf.write(fileName.file.read())
#    buf.seek(0) 
    ofx = ofp.parse(fileName.file)
    for t in ofx.account.statement.transactions:
      tidLink = '<a href=/api/trans/' + t.id.replace(" ", "%20").replace("#", "%23")  + '>' + t.id + '</a>'
      transList.append({'id':t.id, 'link':tidLink, 'amount':t.amount, 'checknum':t.checknum, 'date':t.date, 'mcc':t.mcc, 'memo':t.memo, 'payee':t.payee, 'sic':t.sic, 'type':t.type, 'cat':''})

    df = pandas.DataFrame.from_records(transList, index='id')
    df.amount = df.amount.astype(float)
    return df
  except IOError:
    return "File not found!"
  except ofpe:
    return "Likely an empty file but an OfxParserException was raised!" 
  except ValueError:
    return "Bad OFX File or other ValueError"

def pickleDataFrame(ofxDataFrame):
  '''Write out a the master pickled dataframe.'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  pickleFullName = os.path.join("data", "master.pkl") 
  ofxDataFrame.to_pickle(pickleFullName)
