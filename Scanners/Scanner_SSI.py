from Scanners.Scanner_Base import ScannerBase
from datetime import datetime
from DataStructures.ScannerDataPoint import ScannerDataPoint

class Scanner_SSI(ScannerBase):    
    def sendSignalUpdate(self,  x, y, SignalStrength):
        timestamp=datetime.utcnow()
        datapoint=ScannerDataPoint(timestamp, x, y, SignalStrength)
        self.UpdateSignal.emit(datapoint)
 
    def runscan(self):
        if not self.keepRunning:
            return
            
        self.driver.parkScanner()
        x=self.driver.getXHome()
        y=self.driver.getYHome()
        while self.keepRunning:
            ssi=self.driver.getSignalStrength(80)
            self.sendSignalUpdate(x, y, ssi)  
    
