#!/usr/bin/python
import cherrypy
import finaLib as fl

class fina(object):
  exposed = True
  @cherrypy.tools.accept(media='text/plain')
  
  def GET(self, tid=None, cat=None, graph=None, graphType=None, sortby=None, startDate=None, endDate=None):
    if tid == None and startDate ==None:
      dFrame, dFrameHTML = fl.finaDisp.dispOFX(fl.finaExp.unPickleData())
      return dFrameHTML
    elif (startDate != None) & (endDate != None):
      dFrame, dFrameHTML = fl.finaDisp.dispOFX(fl.finaExp.unPickleData()) 
      slicedDFrame, slicedDFrameHTML = fl.finaDisp.dispDFrameByDate(startDate, endDate, fl.finaExp.unPickleData())
      return slicedDFrameHTML
    else:
      return "Get the trans with id = " + tid
    

  def POST(self, tid=None, payee=None, cat=None, startDate=None, endDate=None):
    if tid == None:
      fl.finaUpdt.updateCat(payee, cat, fl.finaExp.unPickleData())  
      return "Category " + cat + " set for payee " + payee
    else:
      return "Update category for a single transition with tid = " + tid

  def PUT(self, tFile=None):
    fl.finaImp.pickleDataFrame(fl.finaImp.importOFX(tFile))
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
