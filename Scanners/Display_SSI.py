from Scanners.Ui_Display_SSI import Ui_Display_SSI
from Scanners.Scanner_SSI import Scanner_SSI
from PyQt5.QtWidgets import QWidget
from Scanners.Display_Base import Display_Base

class Display_SSI(Ui_Display_SSI,  Display_Base):

    def setupUi(self, parent):
        super(Display_SSI, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        if not self.driver is None:
            self.Polarisation.addItems(self.driver.getPolarizationList())
            self.SamplingRate.addItems(self.driver.getSamplingRatesList())
            self.Band.addItems(self.driver.getFrequencyBandsList())
        
    def stop(self):
        if self.scanner != None:
            self.scanner.cancelScan()
            self.scanner=None
    
    def run(self):
        if self.scanner!=None:
            return
        self.scanner=Scanner_SSI(self.driver, self.spinBox_Averaging.value())
        self.scanner.UpdateSignal.connect(self.displaySSI)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()
        
    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)
        
    def displaySSI(self, scannerData):
        self.label_SSI.setText(str(scannerData.Value) + self.driver.getSSIUnit())
