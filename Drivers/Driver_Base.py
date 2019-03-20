
class Driver_Base (object):
    def  __init__(self):
        self.samplingrates=[]
        self.samplingrateinex=0
        self.frequencyBands=[]
        self.frequencybandindex=0
        self.polarizations=[]
        self.polarisationindex=0
        self.x_home=0
        self.y_home=0
        self.x_max=0
        self.y_max=0

    def ReadParametersFromDevice(self):
        self.samplingrates=self.__splitOptionStringToList(self.__ReadSamplingRateStringFromDevice())
        self.frequencyBands=self.__splitOptionStringToList(self.__ReadFrequencyBandsStringFromDevice)
        self.polarizations=self.__splitOptionStringToList(self.__ReadPolarizationsStringFromDevice())
        self.polarisationindex=self.__GetPolarizationIndexFromDevice()
        self.frequencybandindex=self.__GetFrequencyBandIndexFromDevice()
        self.samplingrateinex= self.__GetSamplingRateIndexFromDevice()
        self.ReadInitialValues()

    def __splitOptionStringToList(self, StringToSplit):
        if not StringToSplit:
            return []
        items=StringToSplit.split(",")
        return items;

    def ReadInitialValues(self):
        pass

    def initializedOK(self):
        pass

    def prepareForOperation(self):
        pass

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

    def __GetPolarizationIndexFromDevice(self):
        #Implement in the derived class
        return ""
        
    def __GetFrequencyBandIndexFromDevice(self):
        #Implement in the derived class
        return "" 
        
    def __GetSamplingRateIndexFromDevice(self):
        #Implement in the derived class
        return "" 
    

    
    
