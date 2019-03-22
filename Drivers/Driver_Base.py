from PyQt5.QtWidgets import QWidget
from abc import  abstractmethod
from Drivers.Wedgies import MetaQWidgetWedgie

class Driver_Base (QWidget, metaclass=MetaQWidgetWedgie):
    def  __init__(self):
        self.samplingrates=[]
        self.samplingrateindex=0
        self.frequencyBands=[]
        self.frequencybandindex=0
        self.polarizations=[]
        self.polarisationindex=0
        self.SSIUnit=""
        self.x_home=0
        self.y_home=0
        self.x_max=0
        self.y_max=0

    def getXHome(self):
        return self.x_home
        
    def getYHome(self):
        return self.y_home    
        
    def getXRange(self):
        return self.x_max
        
    def getYRange(self):
        return self.y_max    

    def getSamplingRatesList(self):
        return self.samplingrates
    
    def getSamplingRate_SelectedIndex(self):
        return self.samplingrateindex
        
    def getPolarizationList(self):
        return self.polarizations
        
    def getPolarization_SelectedIndex(self):
        return self.polarisationindex
    
    def getFrequencyBandsList(self):
        return self.frequencyBands
    
    def getFrequencyBands_SelectedIndex(self):
        return self.frequencybandindex
        
    def getSSIUnit(self):
        return self.SSIUnit

    def ReadParametersFromDevice(self):
        self.samplingrates=self.__splitOptionStringToList(self.ReadSamplingRateStringFromDevice())
        self.frequencyBands=self.__splitOptionStringToList(self.ReadFrequencyBandsStringFromDevice())
        self.polarizations=self.__splitOptionStringToList(self.ReadPolarizationsStringFromDevice())
        self.polarisationindex=self.GetPolarizationIndexFromDevice()
        self.frequencybandindex=self.GetFrequencyBandIndexFromDevice()
        self.samplingrateindex= self.GetSamplingRateIndexFromDevice()
        self.SSIUnit=self.GetSSIUnitFromDevice()
        self.ReadInitialValues()

    def __splitOptionStringToList(self, StringToSplit):
        if not StringToSplit:
            return []
        items=StringToSplit.split(",")
        return items

    @abstractmethod
    def ReadInitialValues(self):
        pass

    @abstractmethod
    def initializedOK(self):
        pass

    @abstractmethod
    def prepareForOperation(self):
        pass

##############
##  Queries
##############

    @abstractmethod
    def ReadSamplingRateStringFromDevice(self):
        #Implement in the derived class
        return ""

    @abstractmethod
    def ReadFrequencyBandsStringFromDevice(self):
        #Implement in the derived class
        return ""    
        
    @abstractmethod
    def ReadPolarizationsStringFromDevice(self):
        #Implement in the derived class
        return "" 

    @abstractmethod
    def GetPolarizationIndexFromDevice(self):
        #Implement in the derived class
        return ""
    
    @abstractmethod
    def GetFrequencyBandIndexFromDevice(self):
        #Implement in the derived class
        return "" 
        
    @abstractmethod        
    def GetSamplingRateIndexFromDevice(self):
        #Implement in the derived class
        return "" 
    
    @abstractmethod        
    def GetSSIUnitFromDevice(self):
        #Implement in the derived class
        return "" 
        
##############
##  Commands
##############

    @abstractmethod
    def SetSamplingRate_Index(self,  SamplingRateIndex):
        pass
        
    @abstractmethod
    def SetPolarizationIndex(self,  PolarizationIndex):
        pass
    
    @abstractmethod
    def SetFrequencyBandIndex(self,  BandIndex):
        pass

    @abstractmethod
    def parkScanner(self):
        pass

    @abstractmethod        
    def moveX(self, XCoord):
        pass

    @abstractmethod        
    def moveY(self, YCoord):
        pass

    
    
