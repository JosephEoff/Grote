from Scanners.Ui_Display_SSI import Ui_Display_SSI
from Scanners.Scanner_SSI import Scanner_SSI
from PyQt5.QtWidgets import QWidget
from Scanners.Display_Base import Display_Base

class Display_SSI(Ui_Display_SSI,  Display_Base):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.setupUi(parent)
        self.scanner=None
        self.scannerThread=None

    def setupUi(self, parent):
        super(Display_SSI, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        
    def stop(self):
        if self.scanner != None:
            self.scanner.cancelScan()
            self.scanner=None
    
    def run(self):
        if self.scanner!=None:
            return
        self.scanner=Scanner_SSI(self.selector.getDriver(), 1)
        self.scanner.UpdateSignal.connect(self.displaySSI)
        self.scanner.ErrorSignal.connect(self.handleError)
        self.scanner.start()
        
    def handleError(self, errormessage):
        self.ShowErrorMessage(errormessage)
        
    def displaySSI(self, scannerData):
        self.label_SSI.setText(str(scannerData.Value))
