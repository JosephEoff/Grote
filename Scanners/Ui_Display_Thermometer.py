# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Scanners/Display_Thermometer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Display_Thermometer(object):
    def setupUi(self, Display_Thermometer):
        Display_Thermometer.setObjectName("Display_Thermometer")
        Display_Thermometer.resize(202, 174)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Display_Thermometer.sizePolicy().hasHeightForWidth())
        Display_Thermometer.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Display_Thermometer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Display_Thermometer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTemperature = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTemperature.sizePolicy().hasHeightForWidth())
        self.labelTemperature.setSizePolicy(sizePolicy)
        self.labelTemperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTemperature.setObjectName("labelTemperature")
        self.gridLayout.addWidget(self.labelTemperature, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.comboBoxUnit = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUnit.sizePolicy().hasHeightForWidth())
        self.comboBoxUnit.setSizePolicy(sizePolicy)
        self.comboBoxUnit.setMaxVisibleItems(3)
        self.comboBoxUnit.setObjectName("comboBoxUnit")
        self.comboBoxUnit.addItem("")
        self.comboBoxUnit.addItem("")
        self.comboBoxUnit.addItem("")
        self.gridLayout.addWidget(self.comboBoxUnit, 3, 1, 1, 1)
        self.buttonRun = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRun.sizePolicy().hasHeightForWidth())
        self.buttonRun.setSizePolicy(sizePolicy)
        self.buttonRun.setObjectName("buttonRun")
        self.gridLayout.addWidget(self.buttonRun, 0, 0, 1, 1)
        self.buttonStop = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)
        self.buttonStop.setObjectName("buttonStop")
        self.gridLayout.addWidget(self.buttonStop, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Display_Thermometer)
        QtCore.QMetaObject.connectSlotsByName(Display_Thermometer)

    def retranslateUi(self, Display_Thermometer):
        _translate = QtCore.QCoreApplication.translate
        Display_Thermometer.setWindowTitle(_translate("Display_Thermometer", "Form"))
        self.groupBox.setTitle(_translate("Display_Thermometer", "Thermometer"))
        self.labelTemperature.setText(_translate("Display_Thermometer", "0.0"))
        self.label.setText(_translate("Display_Thermometer", "Temperature"))
        self.comboBoxUnit.setItemText(0, _translate("Display_Thermometer", "K"))
        self.comboBoxUnit.setItemText(1, _translate("Display_Thermometer", "C"))
        self.comboBoxUnit.setItemText(2, _translate("Display_Thermometer", "F"))
        self.buttonRun.setText(_translate("Display_Thermometer", "Run"))
        self.buttonStop.setText(_translate("Display_Thermometer", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Display_Thermometer = QtWidgets.QWidget()
    ui = Ui_Display_Thermometer()
    ui.setupUi(Display_Thermometer)
    Display_Thermometer.show()
    sys.exit(app.exec_())

