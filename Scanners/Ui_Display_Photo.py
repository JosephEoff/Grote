# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Grote/Scanners/Display_Photo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Display_Photo(object):
    def setupUi(self, Display_Photo):
        Display_Photo.setObjectName("Display_Photo")
        Display_Photo.resize(361, 808)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Display_Photo.sizePolicy().hasHeightForWidth())
        Display_Photo.setSizePolicy(sizePolicy)
        Display_Photo.setMinimumSize(QtCore.QSize(275, 304))
        self.gridLayout_2 = QtWidgets.QGridLayout(Display_Photo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_Controls = QtWidgets.QGroupBox(Display_Photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Controls.sizePolicy().hasHeightForWidth())
        self.groupBox_Controls.setSizePolicy(sizePolicy)
        self.groupBox_Controls.setObjectName("groupBox_Controls")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Controls)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_Averaging = QtWidgets.QSpinBox(self.groupBox_Controls)
        self.spinBox_Averaging.setMinimum(1)
        self.spinBox_Averaging.setObjectName("spinBox_Averaging")
        self.gridLayout.addWidget(self.spinBox_Averaging, 4, 1, 1, 1)
        self.SamplingRate = QtWidgets.QComboBox(self.groupBox_Controls)
        self.SamplingRate.setObjectName("SamplingRate")
        self.gridLayout.addWidget(self.SamplingRate, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_Controls)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.buttonStop = QtWidgets.QPushButton(self.groupBox_Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)
        self.buttonStop.setObjectName("buttonStop")
        self.gridLayout.addWidget(self.buttonStop, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_Controls)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.Band = QtWidgets.QComboBox(self.groupBox_Controls)
        self.Band.setObjectName("Band")
        self.gridLayout.addWidget(self.Band, 2, 1, 1, 1)
        self.buttonRun = QtWidgets.QPushButton(self.groupBox_Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRun.sizePolicy().hasHeightForWidth())
        self.buttonRun.setSizePolicy(sizePolicy)
        self.buttonRun.setObjectName("buttonRun")
        self.gridLayout.addWidget(self.buttonRun, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_Controls)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_Controls)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.Polarisation = QtWidgets.QComboBox(self.groupBox_Controls)
        self.Polarisation.setObjectName("Polarisation")
        self.gridLayout.addWidget(self.Polarisation, 1, 1, 1, 1)
        self.groupBox_Display = QtWidgets.QGroupBox(self.groupBox_Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Display.sizePolicy().hasHeightForWidth())
        self.groupBox_Display.setSizePolicy(sizePolicy)
        self.groupBox_Display.setObjectName("groupBox_Display")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_Display)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview = ImageView(self.groupBox_Display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setObjectName("preview")
        self.horizontalLayout.addWidget(self.preview)
        self.gridLayout.addWidget(self.groupBox_Display, 6, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_Controls, 0, 0, 1, 1)

        self.retranslateUi(Display_Photo)
        QtCore.QMetaObject.connectSlotsByName(Display_Photo)

    def retranslateUi(self, Display_Photo):
        _translate = QtCore.QCoreApplication.translate
        Display_Photo.setWindowTitle(_translate("Display_Photo", "Form"))
        self.groupBox_Controls.setTitle(_translate("Display_Photo", "RF Photo"))
        self.label.setText(_translate("Display_Photo", "Polarisation"))
        self.buttonStop.setText(_translate("Display_Photo", "Stop"))
        self.label_4.setText(_translate("Display_Photo", "Averaging"))
        self.buttonRun.setText(_translate("Display_Photo", "Run"))
        self.label_3.setText(_translate("Display_Photo", "Band"))
        self.label_5.setText(_translate("Display_Photo", "Sampling rate"))
        self.groupBox_Display.setTitle(_translate("Display_Photo", "Preview"))
from pyqtgraph import ImageView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Display_Photo = QtWidgets.QWidget()
    ui = Ui_Display_Photo()
    ui.setupUi(Display_Photo)
    Display_Photo.show()
    sys.exit(app.exec_())
