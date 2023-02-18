from Scanners.Ui_ScannerSelector import Ui_ScannerSelector
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings,  pyqtSignal , pyqtSlot
from Scanners.Display_SSI import Display_SSI
from Scanners.Display_Thermometer import Display_Thermometer
from Scanners.Display_Photo import Display_Photo

class Scanner_Selector( QWidget,  Ui_ScannerSelector):
    def __init__(self, parent):
        super().__init__(parent)
        self.SettingsGroupName='Scanner'
        self.scanner=None
        self.driver=None
        self.setupUi(self)
    
    def setupUi(self, parent):
        super(Scanner_Selector, self).setupUi(parent)
        self.intializeScannerList()
        self.comboBox.currentIndexChanged.connect(self.triggerSaveSettings)
        self.comboBox.currentIndexChanged.connect(self.changeScanner)        
        self.loadSettings()
        self.changeScanner()
        
    def intializeScannerList(self):
        self.comboBox.addItem('Signal Strength Indicator','Signal Strength Indicator')
        self.comboBox.addItem('Thermometer','Thermometer')
        self.comboBox.addItem('Photo','Photo')
    
    def triggerSaveSettings(self,  index):
        self.saveSettings()
        
    def saveSettings(self ):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        settings.setValue("SelectedScanner",  self.comboBox.currentText())
        settings.endGroup()
        
    def loadSettings(self):
        settings=QSettings()
        settings.beginGroup( self.SettingsGroupName)
        self.loadSetting_ComboBox(settings,  self.comboBox,  "SelectedScanner")
        settings.endGroup()
        
    def loadSetting_ComboBox (self, settings, comboBox,  settingname):
        index=comboBox.findText(settings.value(settingname))
        if index>=0:
            comboBox.setCurrentIndex(index)
    
    def changeScanner(self):
        self.removeScanner()
        if self.comboBox.currentText()=="Signal Strength Indicator":
            self.scanner=Display_SSI(self, self.driver)
        if self.comboBox.currentText()=="Thermometer":
            self.scanner=Display_Thermometer(self, self.driver)
        if self.comboBox.currentText()=="Photo":
            self.scanner=Display_Photo(self, self.driver)
        
        if not self.scanner is None:
            self.verticalLayout_Scanner.addWidget(self.scanner)
            self.scanner.show()
            self.scanner.adjustSize()
            self.adjustSize()
            print(self.verticalLayout_Scanner.indexOf(self.scanner))
            
    def removeScanner(self):
        if self.scanner is None:
            return
        self.scanner.deleteLater()      
        self.scanner=None
        
    def getScanner(self):
        return self.scanner;

    @pyqtSlot(object)
    def ChangeDriver(self,  driver):
        if not driver is None:
            self.driver=driver

    def  serializeData(self):
        pass
    
