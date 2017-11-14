from PyQt5 import  QtWidgets
from PyQt5.QtCore import  QCoreApplication
from PyQt5.QtWidgets import QFileDialog,  QMessageBox

import os
import io
import numpy as np

from Ui_MainWindow import Ui_MainWindow

#Named for Grote Reber, who made the first radio maps of the sky.
#https://en.wikipedia.org/wiki/Grote_Reber

class GroteMainWindow(Ui_MainWindow):
    def __init__(self):
        super(GroteMainWindow, self).__init__()
        QCoreApplication.setOrganizationName("Joseph Eoff")
        QCoreApplication.setApplicationName("Grote");
        
    def setupUi(self, MainWindow):
         super(GroteMainWindow, self).setupUi(MainWindow)
         self.actionImport_CSV.triggered.connect(self.ImportCSV)
         self.actionExit.triggered.connect(MainWindow.close)
         MainWindow.closeEvent=self.closeEvent
         
    def closeEvent(self, event):
        event.accept()
        
    def ShowMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
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
    ui = GroteMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
