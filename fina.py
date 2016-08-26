#!/usr/bin/python
import cherrypy
from finaLib import finaImport as fi 
from finaLib import finaDisp as fd
from finaLib import finaUpdate as fu

class fina(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self, ofxFile="master.pkl", startDate=None, endDate=None):
    dFrame, dFrameHTML = fd.dispOFX(ofxFile) 
    HTML = dFrameHTML
    if startDate != None:
      sDFrame, sDFrameHTML = fd.dispDFrameByDate(startDate, endDate, dFrame)
      HTML = sDFrameHTML
    return HTML

  def POST(self, payeeName=None, catName=None):
    if ((payeeName != None) & (catName != None)):
      fu.updateCat(payeeName, catName)
      return "update complete for " + payeeName +  " to category " + catName

  def PUT(self, ofxFile):
    dFrame = fi.importOFX(ofxFile) 
    fi.pickleDataFrame(dFrame)

  def DELETE(self, thing):
    return "this is a delete" 

cherrypy.config.update("fina.cfg")
if __name__ == '__main__':
  cherrypy.tree.mount(fina(), "/", "fina.cfg")
  cherrypy.engine.start()
  cherrypy.engine.block()
