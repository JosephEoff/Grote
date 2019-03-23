from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from Drivers.CommunicationsError import CommunicationsError
from abc import  abstractmethod
from Scanners.Wedgies import MetaQThreadWedgie

class ScannerBase(QThread,  metaclass=MetaQThreadWedgie):
    UpdateSignal=pyqtSignal(object)
    ErrorSignal=pyqtSignal(object)
    
    def __init__(self, driver, OversamplingCount,  BandIndex=0,  PolarisationIndex=0,  SamplingRateIndex=0): 
        super(ScannerBase, self).__init__()
        self.OversamplingCount=OversamplingCount
        self.currentSamplingRateIndex = SamplingRateIndex
        self.currentBandIndex=BandIndex
        self.currentPolarisationIndex=PolarisationIndex
        self.keepRunning=False
        self.keepRunning=True
        self.driver=driver
        if self.driver == None:
            self.ErrorSignal.emit("Error.  No driver supplied.")
            return

    
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
            self.runscan()
        except CommunicationsError as e:
            self.ErrorSignal.emit("Scan aborted: Communications error: " + e.value)        
        except Exception as e:
           self.ErrorSignal.emit("Scan aborted: Error: "  + str(e))
    
    def SendScannerSettingsToDeviceIfNeeded(self):
        if  self.driver is None:
            return
        
        if not self.driver.getSamplingRate_SelectedIndex() == self.currentSamplingRateIndex:
            self.currentSamplingRateIndex=self.driver.SetSamplingRate_Index(self.currentSamplingRateIndex)
            
        if not self.driver.getPolarization_SelectedIndex()== self.currentPolarisationIndex:
            self.currentPolarisationIndex=self.driver.SetPolarizationIndex(self.currentPolarisationIndex)
            
        if not self.driver.getFrequencyBands_SelectedIndex()==self.currentBandIndex:
            self.currentBandIndex=self.driver.SetFrequencyBandIndex(self.currentBandIndex)
        
    def ChangePolarisation(self, polarizationIndex):
        self.currentPolarisationIndex=polarizationIndex
    
    def ChangeBand(self, bandIndex):
        self.currentBandIndex=bandIndex
    
    def ChangeSamplingRate(self,  samplingRateIndex):
        self.currentSamplingRateIndex=samplingRateIndex
    
    def ChangeAveraging(self,  currentAveraging):
        self.OversamplingCount=currentAveraging
        
    @abstractmethod
    def runscan(self):
        #override and implement
        pass
    
