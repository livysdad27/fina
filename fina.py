#!/usr/bin/python
import cherrypy
from finaLib import finaImport as fi 

class fina(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self, thing):
    return "this is a get" 

  def POST(self, thing):
    return "this is a post"

  def PUT(self, ofxFile):
    pGrid = fi.importOFX(ofxFile) 
    print pGrid
    return pGrid

  def DELETE(self, thing):
    return "this is a delete" 

cherrypy.config.update("fina.cfg")
cherrypy.tree.mount(fina(), "/", "fina.cfg")
cherrypy.engine.start()
cherrypy.engine.block()
