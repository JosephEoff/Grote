from Scanners.Ui_Display_Photo import Ui_Display_Photo
from Scanners.Scanner_Photo import Scanner_Photo
from Scanners.Display_Base import Display_Base
from DataStructures.ScannerData_Base import ScannerData_Base
import numpy as np

class Display_Photo(Ui_Display_Photo,  Display_Base):
    scandata = ScannerData_Base(None)
    picturearray = np.zeros((1, 1))
    
    def setupUi(self, parent):
        super(Display_Photo, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        self.Polarisation.currentIndexChanged.connect(self.ChangePolarisation)
        self.SamplingRate.currentIndexChanged.connect(self.ChangeSamplingRate)
        self.Band.currentIndexChanged.connect(self.ChangeBand)
        self.spinBox_Averaging.valueChanged.connect(self.ChangeAveraging)
        self.preview.adjustSize()
        self.groupBox_Display.adjustSize()
        self.groupBox_Controls.adjustSize()
        self.adjustSize()
        
        if not self.driver is None:
            self.Polarisation.addItems(self.driver.getPolarizationList())
            self.SamplingRate.addItems(self.driver.getSamplingRatesList())
            self.Band.addItems(self.driver.getFrequencyBandsList())
    
    def stop(self):
        if self.scanner is not None:
            self.scanner.cancelScan()
            self.scanner = None

    def run(self):
        self.stop()
        self.preview.view.invertY(False)
        self.picturearray = np.zeros((self.driver.getXRange(), self.driver.getYRange()))
        self.preview.setImage(self.picturearray)
        self.preview.adjustSize()
        self.groupBox_Display.adjustSize()
        self.groupBox_Controls.adjustSize()
        self.adjustSize()
        self.scanner = Scanner_Photo(self.driver, self.spinBox_Averaging.value(),  self.Band.currentIndex(),  self.Polarisation.currentIndex(),  self.SamplingRate.currentIndex())
        self.scandata = ScannerData_Base(self.scanner)
        self.scanner.UpdateSignal.connect(self.displayPhoto)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()

    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)

    def displayPhoto(self, scannerData):
        self.scandata.StoreDataPoint(scannerData.Scanner_Coordinate_X,  scannerData)
        self.redrawPhoto(scannerData)
            
    def redrawPhoto(self,  scannerData):
        self.picturearray[scannerData.Scanner_Coordinate_X][scannerData.Scanner_Coordinate_Y] = scannerData.Value
        self.preview.setImage(self.picturearray)
        self.preview.adjustSize()
        self.groupBox_Display.adjustSize()
        self.groupBox_Controls.adjustSize()
        self.adjustSize()

    def  serializeData(self):
        return self.scandata.Serialize()
