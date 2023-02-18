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
        y1 =self.driver.getYHome()
        y2 = self.driver.getYRange()
        step = 1
        for x in range(self.driver.getXHome(), self.driver.getXRange()):
            if not self.keepRunning:
                self.driver.parkScanner()
                return
            self.driver.moveX(x)
#            if x % 2 == 0:
#                y1 =self.driver.getYHome()
#                y2 = self.driver.getYRange()
#                step = 1
#            else:
#                y2 =self.driver.getYHome() -1
#                y1 = self.driver.getYRange() -1
#                step = -1
            for y in range(y1,  y2,  step): 
                if not self.keepRunning:
                    self.driver.parkScanner()
                    return
                self.driver.moveY(y)
                ssi=self.driver.getSignalStrength(self.OversamplingCount)
                self.sendSignalUpdate(x, y, ssi)

            
        self.driver.parkScanner()
