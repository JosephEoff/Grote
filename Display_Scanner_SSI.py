from Ui_Display_Scanner_SSI import Ui_Display_Scanner_SSI
from Scanner_SSI import Scanner_SSI
from PyQt5.QtWidgets import QWidget
from Display_Scanner_Base import Display_Scanner_Base


class Display_Scanner_SSI( QWidget,  Ui_Display_Scanner_SSI,  Display_Scanner_Base):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.scanner=None
        self.scannerThread=None

    def setupUi(self, parent):
        super(Display_Scanner_SSI, self).setupUi(self)
        self.buttonRun.clicked.connect(self.run)
        self.buttonStop.clicked.connect(self.stop)
        
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
