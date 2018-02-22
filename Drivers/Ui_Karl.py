# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Drivers/Karl.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget_Karl(object):
    def setupUi(self, Widget_Karl):
        Widget_Karl.setObjectName("Widget_Karl")
        Widget_Karl.resize(337, 249)
        Widget_Karl.setMinimumSize(QtCore.QSize(100, 50))
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget_Karl)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comportUI = ScannerComport(Widget_Karl)
        self.comportUI.setObjectName("comportUI")
        self.gridLayout.addWidget(self.comportUI, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Widget_Karl)
        QtCore.QMetaObject.connectSlotsByName(Widget_Karl)

    def retranslateUi(self, Widget_Karl):
        _translate = QtCore.QCoreApplication.translate
        Widget_Karl.setWindowTitle(_translate("Widget_Karl", "Form"))

from Drivers.ScannerComport import ScannerComport

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget_Karl = QtWidgets.QWidget()
    ui = Ui_Widget_Karl()
    ui.setupUi(Widget_Karl)
    Widget_Karl.show()
    sys.exit(app.exec_())

