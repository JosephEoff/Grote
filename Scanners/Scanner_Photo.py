from Scanners.Scanner_Base import ScannerBase
from datetime import datetime
from DataStructures.ScannerDataPoint import ScannerDataPoint

class Scanner_Photo(ScannerBase):
    def sendSignalUpdate(self,  x, y, SignalStrength):
        timestamp=datetime.utcnow()
        datapoint=ScannerDataPoint(timestamp, x, y, SignalStrength)
        self.UpdateSignal.emit(datapoint)
 
    def runscan(self):
        if not self.keepRunning:
            return
            
        self.driver.parkScanner()
        self.SendScannerSettingsToDeviceIfNeeded()
        for x in range(self.driver.getXHome(), self.driver.getXRange()):
            if not self.keepRunning:
                return
            self.driver.moveX(x)
            for y in range(self.driver.getYHome(), self.driver.getYRange() ,  1): 
                if not self.keepRunning:
                    return
                self.driver.moveY(y)
                ssi=self.driver.getSignalStrength(self.OversamplingCount)
                self.sendSignalUpdate(x, y, ssi)

        self.driver.parkScanner()
