from PyQt5.QtWidgets import  QMessageBox

class Display_Base(object):
        
    def ShowErrorMessage(self, message):
        self.stop()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok )
        msg.exec_()        
        
    def stop(self):
        #Overwrite in derived class
        pass
        
    def run(self):
        pass
