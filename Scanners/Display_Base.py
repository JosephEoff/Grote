from PyQt5.QtWidgets import  QMessageBox,  QWidget
from abc import  abstractmethod
from Scanners.Wedgies import MetaQWidgetWedgie

    
class Display_Base(QWidget, metaclass=MetaQWidgetWedgie):
    def __init__(self, parent,  driver):
        super(QWidget, self).__init__(parent)
        self.driver=driver
        
        if not self.driver is None:
            self.driver.prepareForOperation()
            if self.driver.initializedOK():
                self.driver.ReadParametersFromDevice()

        self.setupUi(parent)
        self.scanner=None
        self.scannerThread=None
       
    def ShowErrorMessage(self, message):
        self.stop()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok )
        msg.exec_()        
        
    @abstractmethod
    def stop(self):
        #Overwrite in derived class
        pass
        
    @abstractmethod
    def run(self):
        pass
