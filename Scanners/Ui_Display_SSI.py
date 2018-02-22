# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Scanners/Display_SSI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Display_SSI(object):
    def setupUi(self, Display_SSI):
        Display_SSI.setObjectName("Display_SSI")
        Display_SSI.resize(226, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Display_SSI.sizePolicy().hasHeightForWidth())
        Display_SSI.setSizePolicy(sizePolicy)
        Display_SSI.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(Display_SSI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Display_SSI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_SSI = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_SSI.sizePolicy().hasHeightForWidth())
        self.label_SSI.setSizePolicy(sizePolicy)
        self.label_SSI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_SSI.setObjectName("label_SSI")
        self.gridLayout.addWidget(self.label_SSI, 3, 0, 1, 2)
        self.buttonStop = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)
        self.buttonStop.setObjectName("buttonStop")
        self.gridLayout.addWidget(self.buttonStop, 1, 1, 1, 1)
        self.buttonRun = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRun.sizePolicy().hasHeightForWidth())
        self.buttonRun.setSizePolicy(sizePolicy)
        self.buttonRun.setObjectName("buttonRun")
        self.gridLayout.addWidget(self.buttonRun, 1, 0, 1, 1)
        self.selector = DriverSelector(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selector.sizePolicy().hasHeightForWidth())
        self.selector.setSizePolicy(sizePolicy)
        self.selector.setMinimumSize(QtCore.QSize(0, 10))
        self.selector.setObjectName("selector")
        self.gridLayout.addWidget(self.selector, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Display_SSI)
        QtCore.QMetaObject.connectSlotsByName(Display_SSI)

    def retranslateUi(self, Display_SSI):
        _translate = QtCore.QCoreApplication.translate
        Display_SSI.setWindowTitle(_translate("Display_SSI", "Form"))
        self.groupBox.setTitle(_translate("Display_SSI", "Signal Strength Indicator"))
        self.label_SSI.setText(_translate("Display_SSI", "0.0"))
        self.buttonStop.setText(_translate("Display_SSI", "Stop"))
        self.buttonRun.setText(_translate("Display_SSI", "Run"))
        self.label_2.setText(_translate("Display_SSI", "Signal Strength"))

from Drivers.DriverSelector import DriverSelector

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Display_SSI = QtWidgets.QWidget()
    ui = Ui_Display_SSI()
    ui.setupUi(Display_SSI)
    Display_SSI.show()
    sys.exit(app.exec_())

