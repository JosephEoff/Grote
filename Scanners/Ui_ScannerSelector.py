# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Scanners/ScannerSelector.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScannerSelector(object):
    def setupUi(self, ScannerSelector):
        ScannerSelector.setObjectName("ScannerSelector")
        ScannerSelector.resize(312, 244)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScannerSelector.sizePolicy().hasHeightForWidth())
        ScannerSelector.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ScannerSelector)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_Scanner = QtWidgets.QVBoxLayout()
        self.verticalLayout_Scanner.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_Scanner.setObjectName("verticalLayout_Scanner")
        self.comboBox = QtWidgets.QComboBox(ScannerSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 32))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_Scanner.addWidget(self.comboBox, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.verticalLayout_Scanner)

        self.retranslateUi(ScannerSelector)
        QtCore.QMetaObject.connectSlotsByName(ScannerSelector)

    def retranslateUi(self, ScannerSelector):
        _translate = QtCore.QCoreApplication.translate
        ScannerSelector.setWindowTitle(_translate("ScannerSelector", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScannerSelector = QtWidgets.QWidget()
    ui = Ui_ScannerSelector()
    ui.setupUi(ScannerSelector)
    ScannerSelector.show()
    sys.exit(app.exec_())
