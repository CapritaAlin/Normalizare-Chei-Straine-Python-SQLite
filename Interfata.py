# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfata.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 561, 171))
        self.tableWidget.setColumnCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 20, 291, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SelecteazaTabelul = QtWidgets.QComboBox(self.groupBox_3)
        self.SelecteazaTabelul.setGeometry(QtCore.QRect(20, 20, 251, 22))
        self.SelecteazaTabelul.setObjectName("SelecteazaTabelul")
        self.SelecteazaTab = QtWidgets.QPushButton(self.groupBox_3)
        self.SelecteazaTab.setGeometry(QtCore.QRect(90, 50, 91, 23))
        self.SelecteazaTab.setObjectName("SelecteazaTab")
        self.AfiseazaChei = QtWidgets.QPushButton(self.centralwidget)
        self.AfiseazaChei.setGeometry(QtCore.QRect(440, 300, 171, 41))
        self.AfiseazaChei.setObjectName("AfiseazaChei")
        self.Iesire = QtWidgets.QPushButton(self.centralwidget)
        self.Iesire.setGeometry(QtCore.QRect(450, 450, 181, 41))
        self.Iesire.setObjectName("Iesire")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 301, 80))
        self.groupBox.setObjectName("groupBox")
        self.ButonConectare = QtWidgets.QPushButton(self.groupBox)
        self.ButonConectare.setGeometry(QtCore.QRect(100, 50, 91, 23))
        self.ButonConectare.setObjectName("ButonConectare")
        self.Numelebazei = QtWidgets.QLabel(self.groupBox)
        self.Numelebazei.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.Numelebazei.setObjectName("Numelebazei")
        self.NumeBaza = QtWidgets.QLineEdit(self.groupBox)
        self.NumeBaza.setGeometry(QtCore.QRect(120, 20, 161, 20))
        self.NumeBaza.setObjectName("NumeBaza")
        self.CheiePrimara = QtWidgets.QComboBox(self.centralwidget)
        self.CheiePrimara.setGeometry(QtCore.QRect(30, 390, 161, 22))
        self.CheiePrimara.setObjectName("CheiePrimara")
        self.chei = QtWidgets.QComboBox(self.centralwidget)
        self.chei.setGeometry(QtCore.QRect(470, 390, 161, 22))
        self.chei.setObjectName("chei")
        self.tabel = QtWidgets.QComboBox(self.centralwidget)
        self.tabel.setGeometry(QtCore.QRect(270, 391, 141, 21))
        self.tabel.setObjectName("tabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 360, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 360, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 370, 101, 16))
        self.label_3.setObjectName("label_3")
        self.AdaugaConstrangere = QtWidgets.QPushButton(self.centralwidget)
        self.AdaugaConstrangere.setGeometry(QtCore.QRect(240, 450, 171, 41))
        self.AdaugaConstrangere.setObjectName("AdaugaConstrangere")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Selecteaza tabelul"))
        self.SelecteazaTab.setText(_translate("MainWindow", "Selecteaza"))
        self.AfiseazaChei.setText(_translate("MainWindow", "Afiseaza cheile"))
        self.Iesire.setText(_translate("MainWindow", "Iesire"))
        self.groupBox.setTitle(_translate("MainWindow", "Conexiune"))
        self.ButonConectare.setText(_translate("MainWindow", "Conectare"))
        self.Numelebazei.setText(_translate("MainWindow", "Numele bazei de date"))
        self.label.setText(_translate("MainWindow", "Cheia primara a tabelului curent"))
        self.label_2.setText(_translate("MainWindow", "Adauga constrangere pe tabelul"))
        self.label_3.setText(_translate("MainWindow", "Tabele disponibile"))
        self.AdaugaConstrangere.setText(_translate("MainWindow", "Adauga Cheie Straina"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
