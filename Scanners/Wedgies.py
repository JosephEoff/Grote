from abc import ABCMeta
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget

class MetaQThreadWedgie(type(QThread),ABCMeta):
    pass
    
class MetaQWidgetWedgie(type(QWidget),ABCMeta):
    pass
