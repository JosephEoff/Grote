from Ui_Display_Scanner_Thermometer import Ui_Display_Scanner_Thermometer
from Scanner_SSI import Scanner_SSI
from PyQt5.QtWidgets import QWidget
from Display_Scanner_Base import Display_Scanner_Base


class Display_Thermometer( QWidget,  Ui_Display_Scanner_Thermometer,  Display_Scanner_Base):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.scanner=None
        self.scannerThread=None
        self.unit=0

    def setupUi(self, parent):
        super(Display_Thermometer, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        self.comboBoxUnit.currentIndexChanged.connect(self.changeUnit)
        
    def changeUnit(self, index):
        if (index>=0 and index<=2):
            self.unit=index
    
    def stop(self):
        if self.scanner != None:
            self.scanner.cancelScan()
            self.scanner=None
            self.comport.releaseComport()
    
    def run(self):
        if self.scanner!=None:
            return
        self.scanner=Scanner_SSI(self.comport.getComport(), 1)
        self.scanner.UpdateSignal.connect(self.displaySSI)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()
        
    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)
        
    def displaySSI(self, scannerData):
        self.label_SSI.setText(str(scannerData.Value))
