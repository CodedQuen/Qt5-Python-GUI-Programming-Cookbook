# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCreateTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 326)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(180, 20, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditDBName.setFont(font)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setGeometry(QtCore.QRect(200, 230, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCreateTable.setFont(font)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 280, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(180, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTableName.setFont(font)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setGeometry(QtCore.QRect(10, 160, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditColumnName.setFont(font)
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.comboBoxDataType.setGeometry(QtCore.QRect(220, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxDataType.setFont(font)
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.comboBoxDataType.addItem("")
        self.comboBoxDataType.addItem("")
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setGeometry(QtCore.QRect(400, 160, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonAddColumn.setFont(font)
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Create Table"))
        self.label_2.setText(_translate("Dialog", "Enter table name"))
        self.label_3.setText(_translate("Dialog", "Column Name"))
        self.label_4.setText(_translate("Dialog", "Data Type"))
        self.comboBoxDataType.setItemText(0, _translate("Dialog", "integer"))
        self.comboBoxDataType.setItemText(1, _translate("Dialog", "text"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Add Column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

