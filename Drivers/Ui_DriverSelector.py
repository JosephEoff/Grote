# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Drivers/DriverSelector.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DriverSelector(object):
    def setupUi(self, DriverSelector):
        DriverSelector.setObjectName("DriverSelector")
        DriverSelector.resize(402, 331)
        self.gridLayout_3 = QtWidgets.QGridLayout(DriverSelector)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBoxDriver = QtWidgets.QGroupBox(DriverSelector)
        self.groupBoxDriver.setObjectName("groupBoxDriver")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxDriver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxDriverSettings = QtWidgets.QGroupBox(self.groupBoxDriver)
        self.groupBoxDriverSettings.setTitle("")
        self.groupBoxDriverSettings.setObjectName("groupBoxDriverSettings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxDriverSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayoutDriver = QtWidgets.QGridLayout()
        self.gridLayoutDriver.setObjectName("gridLayoutDriver")
        self.verticalLayout_2.addLayout(self.gridLayoutDriver)
        self.gridLayout.addWidget(self.groupBoxDriverSettings, 2, 0, 1, 1)
        self.radioButtonShowDriverSettings = QtWidgets.QRadioButton(self.groupBoxDriver)
        self.radioButtonShowDriverSettings.setObjectName("radioButtonShowDriverSettings")
        self.gridLayout.addWidget(self.radioButtonShowDriverSettings, 1, 0, 1, 1)
        self.comboBoxDriverSelector = QtWidgets.QComboBox(self.groupBoxDriver)
        self.comboBoxDriverSelector.setObjectName("comboBoxDriverSelector")
        self.gridLayout.addWidget(self.comboBoxDriverSelector, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addWidget(self.groupBoxDriver, 0, 0, 1, 1)

        self.retranslateUi(DriverSelector)
        QtCore.QMetaObject.connectSlotsByName(DriverSelector)

    def retranslateUi(self, DriverSelector):
        _translate = QtCore.QCoreApplication.translate
        DriverSelector.setWindowTitle(_translate("DriverSelector", "Form"))
        self.groupBoxDriver.setTitle(_translate("DriverSelector", "Driver"))
        self.radioButtonShowDriverSettings.setText(_translate("DriverSelector", "Driver Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DriverSelector = QtWidgets.QWidget()
    ui = Ui_DriverSelector()
    ui.setupUi(DriverSelector)
    DriverSelector.show()
    sys.exit(app.exec_())

