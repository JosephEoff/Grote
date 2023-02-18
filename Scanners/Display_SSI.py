from Scanners.Ui_Display_SSI import Ui_Display_SSI
from Scanners.Scanner_SSI import Scanner_SSI
from Scanners.Display_Base import Display_Base

class Display_SSI(Ui_Display_SSI,  Display_Base):

    def setupUi(self, parent):
        super(Display_SSI, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        self.Polarisation.currentIndexChanged.connect(self.ChangePolarisation)
        self.SamplingRate.currentIndexChanged.connect(self.ChangeSamplingRate)
        self.Band.currentIndexChanged.connect(self.ChangeBand)
        self.spinBox_Averaging.valueChanged.connect(self.ChangeAveraging)
        
        if not self.driver is None:
            self.Polarisation.addItems(self.driver.getPolarizationList())
            self.SamplingRate.addItems(self.driver.getSamplingRatesList())
            self.Band.addItems(self.driver.getFrequencyBandsList())
    
    def stop(self):
        if self.scanner is not None:
            self.scanner.cancelScan()
            self.scanner = None

    def run(self):
        if self.scanner is not None:
            return
        self.scanner = Scanner_SSI(self.driver, self.spinBox_Averaging.value(),  self.Band.currentIndex(),  self.Polarisation.currentIndex(),  self.SamplingRate.currentIndex())
        self.scanner.UpdateSignal.connect(self.displaySSI)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()

    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)

    def displaySSI(self, scannerData):
        self.label_SSI.setText(str(scannerData.Value) + self.driver.getSSIUnit())
        
    def  serializeData(self):
        pass
