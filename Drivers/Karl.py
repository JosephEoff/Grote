from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings
import time

from Drivers.CommunicationsError import CommunicationsError

from Drivers.Ui_Karl import Ui_Widget_Karl
from Drivers.Driver_Base import Driver_Base

class Karl( QWidget , Ui_Widget_Karl,  Driver_Base ):
    def __init__(self,  parent, MaxTimeout_mS=30000):
        super().__init__(parent)
        self.setupUi(self)
        self.REPLY_TIMEOUT_MS=100
        self.SettingsGroupName='ComPort'
        self.ReplyTimeout_mS=MaxTimeout_mS
        self.Cancel=False
        #self.Comport=self.comportUI.getComport()
        if self.comportUI.getComport()==None:
            return
        self.comportUI.getComport().timeout= self.REPLY_TIMEOUT_MS  
        self.comportUI.getComport().write_timeout=self.REPLY_TIMEOUT_MS
        
    def initializedOK(self):
        if self.comportUI.getComport()==None:
            return False
        return self.comportUI.getComport().isOpen()
            
    def prepareForOperation(self):
        self.openComport()
        
    def openComport(self):        
        if self.comportUI.getComport()==None:
            return
        self.comportUI.lockComport()
        #Wait two seconds.  Once the comport has been opened, you have to wait two seconds for the Arduino to be ready
        time.sleep(2)
        
    def ReadInitialValues(self):
        if self.Cancel:
            return
        self.x_home=self.RequestValueFromScanner("QHX")
        if self.Cancel:
            return
        self.y_home=self.RequestValueFromScanner("QHY")
        if self.Cancel:
            return
        self.x_max=self.RequestValueFromScanner("QRX")
        if self.Cancel:
            return
        self.y_max=self.RequestValueFromScanner("QRY")
        if self.Cancel:
            return
    
    def RequestValueFromScanner(self,requeststring):
        valuestring=self.sendcommand(requeststring)
        return int(self.GetValueFromString(requeststring,valuestring))
    
    def RequestValueFromScanner_Parameter(self,requeststring,parameter):
        valuestring=self.sendcommand(requeststring+str(parameter))
        return float(self.GetValueFromString(requeststring,valuestring))
              
    def GetValueFromString(self,requeststring,scanstring):
        value="0"
        answerstring=str.strip(requeststring,"Q")
        if scanstring==None:
            raise CommunicationsError("Expected Response: " + answerstring + " Received: None" )
            return
        if scanstring=="":
            return value
        
        index=-1
        if answerstring in scanstring:
            index=str.index(scanstring,answerstring)
        if (index==0):
            scanstring=scanstring.replace( answerstring,"")
            scanstring=str.strip(scanstring)
            value=scanstring
        else:
            raise CommunicationsError("Expected Response: " + answerstring + " Received: " + scanstring)
        return value
        
    def CancelCommand(self):
        self.Cancel=True
     
    def disconnectDriver(self):
        self.Cancel=True
        if self.comportUI==None:
            return
        self.comportUI.releaseComport()
        
    def sendcommand(self,commandstring):
        if self.comportUI.getComport()==None:
            raise CommunicationsError("No Comport, command not sent: " + commandstring)
            return None
        else:
            try:
                self.comportUI.getComport().write(bytearray(commandstring+chr(13),  'utf-8'))
                self.comportUI.getComport().flush()
            except:
                raise CommunicationsError("Write failed.")
                
            return self.getReply()      
      
    def getReply(self):
        self.Cancel=False
        replystring=''
        waittime=0
        reply=bytearray()
        reply=self.readLine()
        while not self.Cancel and len(reply)==0 and waittime<self.ReplyTimeout_mS:
            reply=self.readLine()
            waittime=waittime+self.REPLY_TIMEOUT_MS
            
        if len(reply)>0:
            replystring=str(reply, encoding='ascii')
        
        print("Received: " + replystring)
        return replystring
        
    def readLine(self):
        reply=bytearray()
        try:
            reply=self.comportUI.getComport().readline()
        except:
            pass
        return reply
        
    def getXHome(self):
        return self.x_home
        
    def getYHome(self):
        return self.y_home    
        
    def getXRange(self):
        return self.x_max
        
    def getYRange(self):
        return self.y_max    
        
    def parkScanner(self):
        self.sendcommand("GH")
        
    def moveX(self, XCoord):
        self.sendcommand("GX"+str(XCoord))
        
    def moveY(self, YCoord):
         self.sendcommand("GY"+str(YCoord))
         
    def getSignalStrength(self, OversamplingCount):
        return self.RequestValueFromScanner_Parameter("QS",OversamplingCount)
         
