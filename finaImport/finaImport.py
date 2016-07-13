#!/usr/bin/python
import os

def importCSV(fileName):
  '''importCSV brings in the CSV transaction file to be analyzed'''
  if not(os.path.exists("data")):
    os.makedirs("data")
  try:
    fileFullName = os.path.join("data", fileName)
    return file(fileFullName)
  except(IOError):
    return "File not found!"
