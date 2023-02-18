from PyQt5 import  QtWidgets
from PyQt5.QtCore import  QCoreApplication
from PyQt5.QtWidgets import QFileDialog,  QMessageBox

import os
import io
import numpy as np
import jsonpickle

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
         self.actionSave.triggered.connect(self.SaveScan)
         self.actionLoad.triggered.connect(self.LoadScan)
         self.actionImport_CSV.triggered.connect(self.ImportCSV)
         self.actionImport_CSV_Convert_dBm_to_mW.triggered.connect(self.ImportCSV_ConvertFromdbm)
         self.actionExit.triggered.connect(MainWindow.close)
         MainWindow.closeEvent=self.closeEvent
         
    def closeEvent(self, event):
        event.accept()
        
    def ShowMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
    def LoadScan(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(None,'Load scan data', os.getenv('HOME'), 'JSON Files (*.json)' )   
            with open(filename, 'r', encoding='utf-8') as datafile:
                data = jsonpickle.decode(datafile.read())
                image = data.GetNumPyArrayFromData()
                self.DataDisplay.view.invertY(False)
                self.DataDisplay.setImage(image)
            
        except:
            self.ShowMessage('Could not open file.')
    
    def SaveScan(self):
        data = self.scanner.getScanner().serializeData()
        if data == None:
            return
        try:
            filename, _ = QFileDialog.getSaveFileName(None,'Save scan data', os.getenv('HOME'), 'JSON Files (*.json)' )   
            with open(filename, 'w', encoding='utf-8') as datafile:
                datafile.write(data)

        except:
            self.ShowMessage('Could not open file.')
            
    def ImportCSV_ConvertFromdbm(self):
        self.ImportCSV(True)
        
    def ImportCSV(self,  ConvertFromdBm=False):
        try:
            filename, _ = QFileDialog.getOpenFileName(None,'Import CSV', os.getenv('HOME'), 'CSV Files (*.csv)' )   
            inputstream = io.open(filename,'rb')
            data=np.genfromtxt(inputstream,delimiter=' ')
            if ConvertFromdBm:
                data=self.ConvertFromdBmTomW(data)
            self.DataDisplay.setImage(data)
        except:
            self.ShowMessage('Could not open file.')
                        
    def ConvertFromdBmTomW(self, data):
        data=data/10
        data=np.power(10, data)
        return data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GroteMainWindow()
    ui.setupUi(MainWindow)
    ui.driver.selectedDriverChanged.connect(ui.scanner.ChangeDriver)
    ui.scanner.ChangeDriver(ui.driver.getDriver())
    MainWindow.show()
    sys.exit(app.exec_())

