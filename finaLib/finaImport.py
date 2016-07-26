#!/usr/bin/python
import os, pandas 

def importCSV(fileName):
  '''importCSV brings in the CSV transaction file to be analyzed'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  try:
    fileFullName = os.path.join("data", fileName)
    return pandas.read_csv(fileFullName)
  except(IOError):
    return "File not found!"
  except:
    return "Bad csv file!"
