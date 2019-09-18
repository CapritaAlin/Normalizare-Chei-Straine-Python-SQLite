import sys
from PyQt5 import QtWidgets
import Interfata
import sqlite3



class MyQtApp(Interfata.Ui_MainWindow,QtWidgets.QMainWindow):


    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.ButonConectare.clicked.connect(self.conexiune)
        self.SelecteazaTab.clicked.connect(self.afiseazaTabel)
        self.AfiseazaChei.clicked.connect(self.cheie)
        self.AdaugaConstrangere.clicked.connect(self.constrangere)
        self.Iesire.clicked.connect(self.iesire)
        
    def conexiune(self):
        conn=sqlite3.connect(self.NumeBaza.text())
        c=conn.cursor()
        self.SelecteazaTabelul.clear()
        query="SELECT name FROM sqlite_master WHERE type='table';"
        c.execute(query)
        for i in c:
            self.SelecteazaTabelul.addItems(i)

    def afiseazaTabel(self):
        conn=sqlite3.connect(self.NumeBaza.text())
        c=conn.cursor()
        self.tableWidget.clear()
        bd=self.SelecteazaTabelul.currentText()
        query="SELECT * FROM "+bd
        rez=c.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(rez):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def cheie(self):
        self.chei.clear()
        self.CheiePrimara.clear()
        conn=sqlite3.connect(self.NumeBaza.text())
        c=conn.cursor()
        prim=" and name != '"+self.SelecteazaTabelul.currentText()+"'"
        query="SELECT name FROM sqlite_master WHERE type='table'"+prim+";"
        c.execute(query)
        for i in c:
            self.tabel.addItems(i)
        
        if self.SelecteazaTabelul.currentText()=='test':
            self.CheiePrimara.addItem('id')
            self.chei.addItem('a')
            self.chei.addItem('assdcs')
            self.chei.addItem('efefe')
        elif self.SelecteazaTabelul.currentText()=='projects':
            self.CheiePrimara.addItem('')
            self.chei.addItem('a')
            self.chei.addItem('assdcs')
            self.chei.addItem('efefe')
            self.chei.addItem('id')
        elif self.SelecteazaTabelul.currentText()=='abcd':
            self.CheiePrimara.addItem('assdcs')
            self.chei.addItem('efefe')
            self.chei.addItem('id')
            self.chei.addItem('a')
        elif self.SelecteazaTabelul.currentText()=='cba':
            self.CheiePrimara.addItem('efefe')
            self.chei.addItem('a')
            self.chei.addItem('assdcs')
            self.chei.addItem('id')
        else :
            self.CheiePrimara.addItem('a')
            self.chei.addItem('assdcs')
            self.chei.addItem('id')
            self.chei.addItem('efefe')
        
        
    def constrangere(self):
        conn=sqlite3.connect(self.NumeBaza.text())
        c=conn.cursor()
        if self.SelecteazaTabelul.currentText()=='test':
            query="DROP TABLE test"
            c.execute(query)
            query1="CREATE TABLE test(id INT primary key,tests INT,ceva INT, FOREIGN KEY("+self.CheiePrimara.currentText()+") REFERENCES "+self.SelecteazaTabelul.currentText()+"("+self.chei.currentText()+"));"
            c.execute(query1)
        elif self.SelecteazaTabelul.currentText()=='abdc':
            query="DROP TABLE abcd"
            c.execute(query)
            query1="CREATE TABLE abcd (assdcs INTEGER,eewfe INTEGER,fedf INTEGER,PRIMARY KEY(assdcs), FOREIGN KEY("+self.CheiePrimara.currentText()+") REFERENCES "+self.SelecteazaTabelul.currentText()+"("+self.chei.currentText()+"));"
            c.execute(query1)
        elif self.SelecteazaTabelul.currentText()=='cba':
            query="DROP TABLE cba"
            c.execute(query)
            query1="CREATE TABLE cba (efefe INT primary key,fdfs INT, fedfde INT, FOREIGN KEY("+self.CheiePrimara.currentText()+") REFERENCES "+self.SelecteazaTabelul.currentText()+"("+self.chei.currentText()+"));"
            c.execute(quey1)
        elif self.SelecteazaTabelul.currentText()=='sgbd':
            query="DROP TABLE sgbd"
            c.execute(query)
            query1="CREATE TABLE sgbd (a INT primary key,b INT, c INT, FOREIGN KEY("+self.CheiePrimara.currentText()+") REFERENCES "+self.SelecteazaTabelul.currentText()+"("+self.chei.currentText()+"));"
            c.execute(quey1)
        else :print('----')
            
            
        self.chei.clear()
        self.CheiePrimara.clear()
        self.tabel.clear()

    def iesire(self):
        MyQtApp().destroy()
        

        
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    qt_app=MyQtApp()
    qt_app.show()
    app.exec_()
