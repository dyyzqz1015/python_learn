#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 8:47
# @Author  : QinZai
# @File    : Table_UI.py
# @Software: PyCharm

import sys


from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, \
QComboBox, QFrame
from PyQt5.QtGui import QFont, QColor, QBrush, QPixmap

qtCreatorFile = "form.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DomeUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # a = self.lineEdit.text()  # 获取单行输入框内的值
        # self.textEdit.setText('1213')  # 将单行输入框内的值，显示到多长输入框内\
        # self.lineEdit.setText('2323')
        # self.comboBox.addItem("男")
        # self.comboBox.addItem("女")
        # b=("1","2")
        # self.comboBox.addItem(b)

        # horizontalHeader = ["编号1", "姓名1", "性别1", "年龄1", "职业1"]
        Col=self.table.setColumnCount(5)
        Row=self.table.setRowCount(100)

        # self.table.setHorizontalHeaderLabels(horizontalHeader)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectColumns)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.table.setColumnWidth(4, 100)
        self.table.setRowHeight(0, 40)

        for i in range(20):

            self.table.setItem(i, 0, QTableWidgetItem('00'+str(i+1)))
            self.table.setItem(i, 1, QTableWidgetItem("刘亦菲"))
            genderComb = QComboBox()
            genderComb.addItem("男")
            genderComb.addItem("女")
            genderComb.setCurrentIndex(1)
            self.table.setCellWidget(i, 2, genderComb)
            self.table.setItem(i, 3, QTableWidgetItem("30"))
            self.table.setItem(i, 4, QTableWidgetItem("演员"))

        # self.table.setItem(1, 0, QTableWidgetItem("002"))
        # self.table.setItem(1, 1, QTableWidgetItem("马云"))
        # genderComb = QComboBox()
        # genderComb.addItem("男")
        # genderComb.addItem("女")
        # genderComb.setCurrentIndex(0)
        # self.table.setCellWidget(1, 2, genderComb)
        # self.table.setItem(1, 3, QTableWidgetItem("50"))
        # self.table.setItem(1, 4, QTableWidgetItem("企业家"))

        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)

        # self.resize(600, 280)
        # self.center()
        self.setWindowTitle("TableWidget Excempt")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())