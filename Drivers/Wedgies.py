from PyQt5.QtWidgets import QWidget
from abc import ABCMeta

class MetaQWidgetWedgie(type(QWidget),ABCMeta):
    pass
