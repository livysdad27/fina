#!/usr/bin/python
import os, pandas

def dispOFX(fileName="master.pkl"):
  '''importOFX brings in the OFX transaction objects to be analyzed'''
  try:
    if not(os.path.exists("data")):
      os.makedirs("data")
  except(IOError):
    return "Couldn't create data directory!"
  try:
    fileFullName = os.path.join("data", fileName)
    dFrame = pandas.read_pickle(fileFullName)
    dFrameHTML = dFrame.to_html()
    return dFrame, dFrameHTML
  except(IOError):
    return "File not found!"
  except:
    return "Bad pkl file!"
