from Scanners.Ui_Display_Photo import Ui_Display_Photo
from Scanners.Scanner_Photo import Scanner_Photo
from Scanners.Display_Base import Display_Base
from DataStructures.ScannerDataColumn import ScannerDataColumn
import numpy as np

class Display_Photo(Ui_Display_Photo,  Display_Base):
    datadictionary = dict()
    picturearray = np.empty((1, 1))
    
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
        if self.scanner is not None:
            return
        self.picturearray = np.empty((self.driver.getXRange(), self.driver.getXRange()))
        self.preview.setImage(self.picturearray)
        self.preview.adjustSize()
        self.groupBox_Display.adjustSize()
        self.groupBox_Controls.adjustSize()
        self.adjustSize()
        self.datadictionary = dict()
        self.scanner = Scanner_Photo(self.driver, self.spinBox_Averaging.value(),  self.Band.currentIndex(),  self.Polarisation.currentIndex(),  self.SamplingRate.currentIndex())
        self.scanner.UpdateSignal.connect(self.displayPhoto)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()

    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)

    def displayPhoto(self, scannerData):
        if  not scannerData.Scanner_Coordinate_X in self.datadictionary:
            datacolumn = ScannerDataColumn()
            self.datadictionary[scannerData.Scanner_Coordinate_X] = datacolumn
        self.datadictionary[scannerData.Scanner_Coordinate_X].AddDataPoint(scannerData)
        self.redrawPhoto(scannerData)
            
    def redrawPhoto(self,  scannerData):
        self.picturearray[scannerData.Scanner_Coordinate_X][scannerData.Scanner_Coordinate_Y] = scannerData.Value
        self.preview.setImage(self.picturearray)
        self.preview.adjustSize()
        self.preview.view.invertY(False)
        self.groupBox_Display.adjustSize()
        self.groupBox_Controls.adjustSize()
        self.adjustSize()
