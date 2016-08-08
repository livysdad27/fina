#!/usr/bin/python
import cherrypy

class fina(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self, thing):
    return "this is a get" 

  def POST(self, thing):
    return "this is a post"

  def PUT(self, thing):
    return "this is a put" 

  def DELETE(self, thing):
    return "this is a delete" 

cherrypy.config.update("fina.cfg")
cherrypy.tree.mount(fina(), "/", "fina.cfg")
cherrypy.engine.start()
cherrypy.engine.block()
