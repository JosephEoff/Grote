class ScannerDataPoint:
    def __init__(self, Timestamp_UTC_DateTime,  Scanner_X,  Scanner_Y,  Value):
        self.Timestamp=Timestamp_UTC_DateTime
        self.Value=Value
        self.Scanner_Coordinate_X=Scanner_X
        self.Scanner_Coordinate_Y=Scanner_Y
