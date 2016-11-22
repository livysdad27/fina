#!/usr/bin/python
import finaImp as fi
import os, pandas, urllib

def updateCat(payeeName, catName, tid, dFrame, dirName="data", pklName="master.pkl" ):
  '''Update a category and re-persist the DataFrame to pickle again'''
  if tid is None:
    dFrame.loc[dFrame['payee'] == payeeName, 'cat'] = catName
    fi.pickleDataFrame(dFrame, pklName, dirName)
    return True
  else:
    tid = urllib.unquote(tid).decode()
    dFrame.loc[dFrame['id'] == tid, 'cat'] = catName
    fi.pickleDataFrame(dFrame, pklName, dirName)
    return True
