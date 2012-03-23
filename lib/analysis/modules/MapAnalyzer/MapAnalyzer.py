from PyQt4 import QtGui, QtCore
import os
from lib.analysis.AnalysisModule import AnalysisModule
from collections import OrderedDict
import pyqtgraph as pg
from metaarray import MetaArray
import numpy as np
import scipy
import functions as fn
#import CellHealthCtrlTemplate
from HelpfulException import HelpfulException
from pyqtgraph.widgets.FileDialog import FileDialog
import sys
from DatabaseGui.DatabaseQueryWidget import DatabaseQueryWidget
from SpatialCorrelator import SpatialCorrelator
from MapConvolver import MapConvolver
from ColorMapper import ColorMapper
from Canvas.items.ImageCanvasItem import ImageCanvasItem





class MapAnalyzer(AnalysisModule):
    
    def __init__(self, host):
        AnalysisModule.__init__(self, host)
        self.dbIdentity = 'Map Analyzer' ## how we identify to the database; this determines which tables we own
        
        modPath = os.path.abspath(os.path.split(__file__)[0])
        
        self._elements_ = OrderedDict([
            ('Database Query', {'type':'ctrl', 'object': DatabaseQueryWidget(self.dataManager()), 'size':(200,200), 'host':self}),
            ('File Loader', {'type':'fileInput', 'pos':('below', 'Database Query'), 'host':self, 'showFileTree':False}),
            ('Map Convolver', {'type':'ctrl', 'object': MapConvolver(), 'size': (200, 200), 'pos':('bottom', 'Database Query')}),
            ('Color Mapper', {'type':'ctrl', 'object': ColorMapper(filePath=os.path.join(modPath, "colorMaps")), 'size': (200,200), 'pos':('right', 'Database Query')}),
            ('Spatial Correlator', {'type':'ctrl', 'object':SpatialCorrelator(), 'size':(100,200), 'pos': ('bottom', 'Map Convolver')}),
            ('Canvas', {'type': 'canvas', 'pos': ('bottom', 'Color Mapper'), 'size': (700,400), 'allowTransforms': False, 'hideCtrl': True, 'args': {'name': 'Map Analyzer'}})
            #('File Loader', {'type': 'fileInput', 'size': (100, 300), 'host': self, 'args': {'showFileTree': True}}),
            #('ctrl', {'type': 'ctrl', 'object': self.ctrlWidget, 'pos': ('bottom', 'File Loader'), 'size': (100, 100)}),
            #('Rs Plot', {'type': 'plot', 'pos':('right', 'File Loader'), 'size':(200, 600), 'labels':{'left':(None,'Ohms'), 'bottom':(None,'s')}}),
            #('Rm Plot', {'type': 'plot', 'pos':('bottom', 'Rs Plot'), 'size':(200, 600),'labels':{'left':(None,'Ohms'), 'bottom':(None,'s')}}),
            #('Ih Plot', {'type': 'plot', 'pos':('bottom', 'Rm Plot'), 'size':(200, 600), 'labels':{'left':(None,'A'), 'bottom':(None, 's')}}),
            #('Traces Plot', {'type': 'plot', 'pos':('right', 'ctrl'), 'size':(200, 600), 'labels':{'left':(None,'A'), 'bottom':(None,'s')}}),
        ])
        self.initializeElements()
        for el in self.getAllElements():
            self.getElement(el, create=True)
            
            
        ## reserve variables that will get set later
        self.imgItem = None
        self.spacing = None
        self.imgData = None
        
        
        self.dbquery = self.getElement("Database Query")
        self.canvas = self.getElement("Canvas")
        self.mapConvolver = self.getElement("Map Convolver")
        self.colorMapper = self.getElement("Color Mapper")
        self.spatialCorrelator = self.getElement("Spatial Correlator")
        
        self.outline = self.spatialCorrelator.getOutline()
        self.canvas.addGraphicsItem(self.outline)
        
        
        self.dbquery.sigTableChanged.connect(self.setData)
        self.mapConvolver.sigOutputChanged.connect(self.convolverOutputChanged)
        self.mapConvolver.sigFieldsChanged.connect(self.giveOptsToCM)
        self.colorMapper.sigChanged.connect(self.computeColors)
        
        
        
    def setData(self):
        data = self.dbquery.table()
        self.getElement("Spatial Correlator").setData(data)
        self.getElement("Map Convolver").setData(data)
        
    def convolverOutputChanged(self, data, spacing):
        self.spacing = spacing
        self.imgData = data
        self.recolorMap(self.colorMapper.getColorArray(data))
        
    def computeColors(self):
        if self.imgData is not None:
            self.recolorMap(self.colorMapper.getColorArray(self.imgData))
        
    def recolorMap(self, data):
        if self.imgItem is None:
            if data is None:
                return
            table = self.dbquery.table()
            x = table['xPos'].min()
            y = table['yPos'].min()
            self.imgItem = ImageCanvasItem(data, pos=(x, y), scale=self.spacing, movable=False, scalable=False, name="ConvolvedMap")
            self.canvas.addItem(self.imgItem)
            return
        self.imgItem.updateImage(data)
            
    def giveOptsToCM(self, fields):
        self.colorMapper.setArgList(fields)
        
    def saveMA(self, fileName=None):
        if self.imgData is None:
            raise HelpfulException("There is no processed data to save.")
        if fileName is None:
            dh = self.getElement("File Loader").baseDir().name()
            self.fileDialog = FileDialog(None, "Save image data", dh, '*.ma')
            self.fileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
            self.fileDialog.show()
            self.fileDialog.fileSelected.connect(self.saveMA)
            return  
        
        table = self.dbquery.table()
        x = table['xPos'].min()
        y = table['yPos'].min()        
        
        #print "params:", self.imgData.dtype.names
        #print "shape:", self.imgData.shape
        #arr = MetaArray(self.currentData) ### need to format this with axes and info
        arr = MetaArray([self.imgData[p] for p in self.imgData.dtype.names], info=[
            {'name':'vals', 'cols':[{'name':p} for p in self.imgData.dtype.names]},
            {'name':'xPos', 'units':'m', 'values':np.arange(self.imgData.shape[0])*self.spacing+x},
            {'name':'yPos', 'units':'m', 'values':np.arange(self.imgData.shape[1])*self.spacing+y},
            
            {'spacing':self.spacing}
        ]) 
        
        arr.write(fileName)    
    
    def loadFileRequested(self, fhList):
        canvas = self.getElement('Canvas')
        model = self.dataModel

        for fh in fhList:
            try:
                ## TODO: use more clever detection of Scan data here.
                if fh.isFile() or model.dirType(fh) == 'Cell':
                    canvas.addFile(fh)
                else:
                    #self.loadScan(fh)
                    debug.printExc("MapAnalyzer does not yet support loading scans")
                    return False
                return True
            except:
                debug.printExc("Error loading file %s" % fh.name())
                return False