#!/usr/bin/python
import os, pandas

def unPickleData(pklFile="master.pkl"):
  '''Unpickle a dataframe so we can do things to it.  Use master.pkl as the default'''
  fullPklFileName=os.path.join("data", pklFile)
  if not(os.path.isfile(fullPklFileName)):
    return "Couldn't find file!"
  else:
    return pandas.read_pickle(fullPklFileName)     
