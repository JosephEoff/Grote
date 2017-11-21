from PyQt5 import QtCore, QtGui, QtWidgets

from Drivers.Ui_ScannerComport import Ui_ScannerComport
import QSerialPortInfo

class ScannerComport(Ui_ScannerComport):
    def __init__(self):
        super(ScannerComport, self).__init__()
        self.InitializePortListControl()
        
    def InitializePortListControl(self):
        available_ports = QSerialPortInfo.availablePorts()
        for port in available_ports:
            if  not port.isBusy:
                 self.comboBox_SerialPort.addItem(port.portName())
        
            
