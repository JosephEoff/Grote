from PyQt5.QtWidgets import  QMessageBox,  QWidget
from abc import  abstractmethod
from Scanners.Wedgies import MetaQWidgetWedgie

    
class Display_Base(QWidget, metaclass=MetaQWidgetWedgie):
        
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
