#!/usr/bin/python
import os

def importCSV(fileName):
  '''importCSV brings in the CSV transaction file to be analyzed'''
  try:
    dataDir = "data" 
    fileFullName = os.path.join(dataDir, fileName)
    return file(fileFullName)
  except(IOError):
    return "File not found!"
