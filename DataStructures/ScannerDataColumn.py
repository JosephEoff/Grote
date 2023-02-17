from DataStructures.ScannerDataPoint import ScannerDataPoint
from datetime import datetime

class ScannerDataColumn:
    def __init__(self):
        self.ColumnData = list()
        self.X = 0
        self.Y = 0
        self.Azimuth = 0.0
        self.Altitude = 0.0
        self.Timestamp = datetime.utcnow()
        
    def Height(self):
        return len(self.ColumnData)
    
    def AddDataPoint(self, DataPoint):
        self.ColumnData.append(DataPoint)
