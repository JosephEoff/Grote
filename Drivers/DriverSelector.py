from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings

from Drivers.Ui_DriverSelector import Ui_DriverSelector
from Drivers.ScannerComport import ScannerComport

class DriverSelector( QWidget,  Ui_DriverSelector):
    def  __init__(self,parent):
       super().__init__(parent)
       self.SettingsGroupName='Driver'
       self.setupUi(self)

    def setupUi(self, parent):
        super(DriverSelector, self).setupUi(parent)
        self.initializeDriverSelectorListl() 
        self.loadSettings()
        self.radioButtonShowDriverSettings.setChecked(True)
        self.radioButtonShowDriverSettings.toggled.connect(self.toggleExpansion)
        self.comboBoxDriverSelector.currentIndexChanged.connect(self.triggerSaveSettings)
        self.comboBoxDriverSelector.currentIndexChanged.connect(self.changeDriver)
        self.changeDriver()
        
    def initializeDriverSelectorListl(self):
        self.comboBoxDriverSelector.addItem("Karl")
        
    def toggleExpansion(self):
        if self.radioButtonShowDriverSettings.isChecked():
            self.groupBoxDriverSettings.show()
        else:
            self.groupBoxDriverSettings.hide()
        
    def triggerSaveSettings(self,  index):
        self.saveSettings()
        
    def saveSettings(self ):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        settings.setValue("SelectedDriver",  self.comboBoxDriverSelector.currentText())
        settings.endGroup()
        
    def loadSettings(self):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        self.loadSetting_ComboBox(settings,  self.comboBoxDriverSelector,  "SelectedDriver")
        settings.endGroup()
        
    def loadSetting_ComboBox (self, settings, comboBox,  settingname):
        index=comboBox.findText(settings.value(settingname))
        if index>=0:
            comboBox.setCurrentIndex(index)
            
    def changeDriver(self):
        self.removeDriver()
        if self.comboBoxDriverSelector.currentText()=="Karl":
            self.gridLayoutDriver.addWidget(ScannerComport(self))
            
    def removeDriver(self):
        while self.gridLayoutDriver.count():
            child = self.gridLayoutDriver.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
