from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from Drivers.CommunicationsError import CommunicationsError
from abc import  abstractmethod
from Scanners.Wedgies import MetaQThreadWedgie

class ScannerBase(QThread,  metaclass=MetaQThreadWedgie):
    UpdateSignal=pyqtSignal(object)
    ErrorSignal=pyqtSignal(object)
    
    def __init__(self, driver, OversamplingCount): 
        super(ScannerBase, self).__init__()
        self.OversamplingCount=OversamplingCount
        self.keepRunning=False
        self.keepRunning=True
        self.driver=driver
    
    def __del__(self):
        self.wait()
        
    def cancelScan(self):
        self.keepRunning=False
        if not self.driver == None:
            self.driver.CancelCommand()
            self.driver.disconnectDriver()

    def run(self):
        if self.driver==None:
            return
        self.driver.prepareForOperation()
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
    
    @abstractmethod
    def runscan(self):
        #override and implement
        pass
    
