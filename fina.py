#!/usr/bin/python
#This is the main Fina API broker
import os
import cherrypy
import finaLib as fl

currentDir = os.path.dirname(os.path.abspath(__file__))

class fina(object):
  exposed = True
  @cherrypy.tools.accept(media='text/plain')
  
  def GET(self, tid=None, cat=None, graph=None, graphType=None, sortby=None, startDate=None, endDate=None, now=None):
    if tid == None and startDate ==None and cat == None and graph ==  None:
      dFrame, dFrameHTML = fl.finaDisp.dispOFX(fl.finaExp.unPickleData())
      return dFrameHTML

    elif (startDate != None) & (endDate != None) & (graph==None):
      slicedDFrame, slicedDFrameHTML = fl.finaDisp.dispDFrameByDate(startDate, endDate, fl.finaExp.unPickleData())
      return slicedDFrameHTML

    elif cat != None and graph == None:
      dFrame, dFrameHTML = fl.finaDisp.dispDFrameByCat(cat, fl.finaExp.unPickleData())
      return dFrameHTML

    elif graph != None:
      if (startDate != None) & (endDate != None):
        dFrame, dFrameHTML = fl.finaDisp.dispDFrameByDate(startDate, endDate, fl.finaExp.unPickleData()) 
        buf = fl.finaDisp.dispPareto(dFrame)
      elif graph == 'pareto':
        buf = fl.finaDisp.dispPareto(fl.finaExp.unPickleData())
      elif graph == 'monthPareto':
        buf = fl.finaDisp.dispMonthPareto(fl.finaExp.unPickleData(), cat)
      buf.seek(0)
      cherrypy.response.headers['Content-Type'] = "image/png"
      return cherrypy.lib.file_generator(buf)

    elif tid != None:
      trans = fl.finaDisp.dispDFrameById(tid, fl.finaExp.unPickleData())
      return trans 

  def POST(self, tid=None, payee=None, cat=None, startDate=None, endDate=None):
    if tid == None:
      fl.finaUpdt.updateCat(payee, cat, None, fl.finaExp.unPickleData())  
      return "Category " + cat + " set for payee " + payee
    else:
      fl.finaUpdt.updateCat(None, cat, tid, fl.finaExp.unPickleData())
      return "Update category for a single transition with tid = " + tid

  def PUT(self, tFile=None):
    fl.finaImp.pickleDataFrame(fl.finaImp.importOFX(tFile.file))
    return "Imported a transaction file"

  def DELETE(self, tid=None):
    if tid == None:
      return "Delete a whole trans file"
    else:
      return "Delte a single transaction with id=" + tid

class home(object):
  pass

cherrypy.config.update("global.cfg")
if __name__ == '__main__':
  cherrypy.tree.mount(fina(), "/api/trans", "fina.cfg")
  cherrypy.tree.mount(home(), "/", "home.cfg")
  cherrypy.engine.start()
  cherrypy.engine.block()
