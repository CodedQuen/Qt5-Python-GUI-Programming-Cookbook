# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTwoProgressBarsAsync.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 269)
        self.progressBarFileDownload = QtWidgets.QProgressBar(Dialog)
        self.progressBarFileDownload.setGeometry(QtCore.QRect(40, 90, 281, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBarFileDownload.setFont(font)
        self.progressBarFileDownload.setProperty("value", 0)
        self.progressBarFileDownload.setObjectName("progressBarFileDownload")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBarVirusScan = QtWidgets.QProgressBar(Dialog)
        self.progressBarVirusScan.setGeometry(QtCore.QRect(40, 230, 281, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBarVirusScan.setFont(font)
        self.progressBarVirusScan.setProperty("value", 0)
        self.progressBarVirusScan.setObjectName("progressBarVirusScan")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(120, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scanning for Virus"))
        self.pushButtonStart.setText(_translate("Dialog", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

