

class Driver_Base (object):
    def  __init__(self):
        self.samplingrates=[]
        self.frequencyBands=[]
        self.polarizations=[]
        self.x_home=0
        self.y_home=0
        self.x_max=0
        self.y_max=0

    def ReadParametersFromDevice(self):
        self.samplingrates=self.__splitOptionStringToList(self.__ReadSamplingRateStringFromDevice())
        self.frequencyBands=self.__splitOptionStringToList(self.__ReadFrequencyBandsStringFromDevice)
        self.polarizations=self.__ReadPolarizationsStringFromDevice
           #Read motion ranges
        #Query current sampling rate
        #query current band
        #query current polarizations
        #Need the current values for display and for further (real) use
        #

    def ReadInitialValues(self):
        pass
        
    def initializedOK(self):
        pass
        
    def prepareForOperation(self):
        pass

    def __splitOptionStringToList(self, StringToSplit):
        if not StringToSplit:
            return []
        items=StringToSplit.split(",")
        return items;
        
    def getSamplingRatesList(self):
        return self.samplingrates
        
    def SetSamplingRate_Index(self,  SamplingRateIndex):
        pass
        
    def __ReadSamplingRateStringFromDevice(self):
        #Implement in the derived class
        return ""
        
    def __ReadFrequencyBandsStringFromDevice(self):
        #Implement in the derived class
        return ""    
        
    def __ReadPolarizationsStringFromDevice(self):
        #Implement in the derived class
        return ""    
    
    
