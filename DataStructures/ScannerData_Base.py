from DataStructures.ScannerDataColumn import ScannerDataColumn
from datetime import datetime
import jsonpickle
import numpy as np

class ScannerData_Base(object):
    def __init__(self,  ScannerObject):
        self.Timestamp = datetime.utcnow()
        self.Width = 0
        self.Height = 0
        self.Azimuth = 0.0
        self.Altitude = 0.0
        self.ScannerColumns = dict()
        self.ScanType = type(ScannerObject)
        
    def StoreDataPoint(self, ColumnID,  DataPoint):
        if  not ColumnID in self.ScannerColumns:
            datacolumn = ScannerDataColumn()
            self.ScannerColumns[ColumnID] = datacolumn
        self.ScannerColumns[ColumnID].AddDataPoint(DataPoint)
        self.Width = len( self.ScannerColumns)
        if (self.ScannerColumns[ColumnID].Height()>self.Height):
            self.Height=self.ScannerColumns[ColumnID].Height()
            
    def Serialize(self):
        if self.ScanType == "None":
            return None
        return jsonpickle.encode(self)

    def GetNumPyArrayFromData(self):
        dataarray = np.empty((self.Height,self.Width))
        for column in self.ScannerColumns:
            for point in self.ScannerColumns[column].ColumnData:
                dataarray[point.Scanner_Coordinate_X][point.Scanner_Coordinate_Y] = point.Value
        return dataarray
    
