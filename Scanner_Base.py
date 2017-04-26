from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from ScannerDriver import ScannerDriver
from CommunicationsError import CommunicationsError

class ScannerBase(QThread):
    UpdateSignal=pyqtSignal(object)
    ErrorSignal=pyqtSignal(object)
    
    def __init__(self, Comport, OversamplingCount): 
        super(ScannerBase, self).__init__()
        self.Comport=Comport
        self.OversamplingCount=OversamplingCount
        self.keepRunning=False
        self.driver=None
        self.keepRunning=True
    
    def __del__(self):
        self.wait()
    
    def cancelScan(self):
        self.keepRunning=False
        if not self.driver == None:
            self.driver.CancelCommand()
            
    def run(self):
        self.driver=ScannerDriver(self.Comport)
        if self.driver.initializedOK():
            self.doRunScan()
        else:
            self.ErrorSignal.emit("Error.  Comport couldn't be opened.  Scan aborted.")
    
    def doRunScan(self):
        try:
            self.driver.ReadInitialValues()
            self.runscan()
        except CommunicationsError as e:
            self.ErrorSignal.emit("Scan aborted: Communications error: " + e.value)        
        except Exception as e:
           self.ErrorSignal.emit("Scan aborted: Error: "  +e.strerror)
    
    def runscan(self):
        #override and implement
        pass
    
