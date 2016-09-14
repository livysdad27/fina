#!/usr/bin/python
import cherrypy
import finaLib as fl

class fina(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self, tid=None, cat=None, graph=None, graphType=None, sortby=None, startDate=None, endDate=None):
    if tid == None and startDate ==None:
      dFrame, dFrameHTML = fl.finaDisp.dispOFX(fl.finaExport.unPickleData())
      return dFrameHTML
    elif (startDate != None) & (endDate != None):
      dFrame, dFrameHTML = fl.finaDisp.dispOFX(fl.finaExport.unPickleData()) 
      slicedDFrame, slicedDFrameHTML = fl.finaDisp.dispDFrameByDate(startDate, endDate, fl.finaExport.unPickleData())
      return slicedDFrameHTML
    else:
      return "Get the trans with id = " + tid
    

  def POST(self, tid=None, payee=None, cat=None, startDate=None, endDate=None):
    if tid == None:
      return "Update categories for a set of transactions"
    else:
      return "Update category for a single transition with tid = " + tid

  def PUT(self, tFile=None):
    finaLib.finaImport.pickleDataFrame(finaLib.finaImport.importOFX(tFile))
    return "Imported a transaction file"

  def DELETE(self, tid=None):
    if tid == None:
      return "Delete a whole trans file"
    else:
      return "Delte a single transaction with id=" + tid
    
cherrypy.config.update("fina.cfg")
if __name__ == '__main__':
  cherrypy.tree.mount(fina(), "/api/trans", "fina.cfg")
  cherrypy.engine.start()
  cherrypy.engine.block()
