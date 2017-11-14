from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings

import serial
import serial.tools.list_ports
import time

from Drivers.Ui_ScannerComport import Ui_ScannerComport

class ScannerComport( QWidget,  Ui_ScannerComport):
    def  __init__(self,parent):
       super().__init__(parent)
       self.SettingsGroupName='ComPort'
       self.setupUi(self)
       self.comport=None 

    def setupUi(self, parent):
        super(ScannerComport, self).setupUi(parent)
        self.initializePortListControl() 
        self.initializeBaudRateControl()
        self.loadSettings()
        self.radioButtonExpand.setChecked(True)
        self.radioButtonExpand.toggled.connect(self.toggleExpansion)
        self.comboBox_BaudRate.currentIndexChanged.connect(self.triggerSaveSettings)
        self.comboBox_SerialPort.currentIndexChanged.connect(self.triggerSaveSettings)
     
    def toggleExpansion(self):
        if self.radioButtonExpand.isChecked():
            self.initializePortListControl()
            self.groupBox_Hider.show()
        else:
            self.groupBox_Hider.hide()

    def triggerSaveSettings(self,  index):
        self.saveSettings()
        
    def saveSettings(self ):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        settings.setValue("PortName", self.comboBox_SerialPort.currentText())
        settings.setValue( "BaudRate", self.comboBox_BaudRate.currentText())
        settings.endGroup()

    def loadSettings(self):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        self.loadSetting_ComboBox(settings,  self.comboBox_BaudRate,  "BaudRate")
        self.loadSetting_ComboBox (settings,  self.comboBox_SerialPort,  "PortName")
        settings.endGroup()

    def loadSetting_ComboBox (self, settings, comboBox,  settingname):
        index=comboBox.findText(settings.value(settingname))
        if index>=0:
            comboBox.setCurrentIndex(index)

    def initializePortListControl(self):
        available_ports = serial.tools.list_ports.comports()
        if len(available_ports)>0:
            self.comboBox_SerialPort.clear()
            for port in available_ports:
                self.comboBox_SerialPort.addItem(port[0])

    def initializeBaudRateControl(self):
        self.comboBox_BaudRate.clear()
        for rate in serial.Serial.BAUDRATES:
            self.comboBox_BaudRate.addItem(str(rate))

    def getComport(self):
        try:            
            self.groupBox_Hider.setEnabled(False)
            self.comport=serial.Serial()
            self.comport.port=self.comboBox_SerialPort.currentText()    
            self.comport.baudrate=int(self.comboBox_BaudRate.currentText())
            self.comport.xonxoff=False
            self.comport.rtscts=False
            self.comport.dsrdtr=False
            self.comport.parity=serial.PARITY_NONE
            self.comport.stopbits=serial.STOPBITS_ONE
            self.comport.databits=serial.EIGHTBITS
            self.comport.dtr=True
            self.comport.open( )   
#         #Arduino Gendenkzeit - homage on the reboot time for the Arduino
            time.sleep(2)
        except:
            self.groupBox_Hider.setEnabled(True)
            self.comport=None
            self.initializePortListControl()
            
        return self.comport

    def releaseComport(self):
        self.groupBox_Hider.setEnabled(True)
        if self.comport!=None:
            self.comport.close()


