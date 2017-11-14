
class ScannerData_Base:
    def __init__(self):
        self.Width=0
        self.Height=0
        self.Azimuth=0.0
        self.Altitude=0.0
        self.ScannerColumns={}
        
    def AddColumn(self,  DataColumn):
        self.ScannerColumns.append(DataColumn)
        self.Width=self.Width+1
        if (DataColumn.Height>self.Height):
            self.Height=DataColumn.Height
            
            
