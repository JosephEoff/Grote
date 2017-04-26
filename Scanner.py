from PyQt5 import  QtWidgets
from PyQt5.QtCore import  QCoreApplication

import os
import io
import numpy as np
from PyQt5.QtWidgets import QFileDialog,  QMessageBox
from Ui_MainWindow import Ui_MainWindow


class ScannerMainWindow(Ui_MainWindow):
    def __init__(self):
        super(ScannerMainWindow, self).__init__()
        QCoreApplication.setOrganizationName("Microwave Scanner")
        QCoreApplication.setApplicationName("Microwave Scanner");
        
    def setupUi(self, MainWindow):
         super(ScannerMainWindow, self).setupUi(MainWindow)
         self.actionImport_CSV.triggered.connect(self.ImportCSV)
         self.actionExit.triggered.connect(MainWindow.close)
         MainWindow.closeEvent=self.closeEvent
         
    def closeEvent(self, event):
        #self.Comport.saveSettings()
        event.accept()
        
    def ShowMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
       # msg.setInformativeText("This is additional information")
        #msg.setWindowTitle("S")
        #msg.setDetailedText("The details are as follows:")
        
    def ImportCSV(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(None,'Import CSV', os.getenv('HOME'), 'CSV Files (*.csv)' )   
            inputstream = io.open(filename,'rb')
            data=np.genfromtxt(inputstream,delimiter=' ')
            self.DataDisplay.setImage(data)
        except:
            self.ShowMessage('Could not open file.')
                        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ScannerMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
