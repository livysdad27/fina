#!/usr/bin/python
import cherrypy
from finaLib import finaImport as fi 
from finaLib import finaDisp as fd

class fina(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self, ofxFile="master.pkl"):
    dFrame, dFrameHTML = fd.dispOFX(ofxFile) 
    return dFrameHTML

  def POST(self, thing):
    return "this is a post"

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
