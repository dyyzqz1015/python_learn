#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 8:37
# @Author  : QinZai
# @File    : Table.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
'''


TableWidget
'''
# __author__ = ‘py40.com’

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, \
QComboBox, QFrame
from PyQt5.QtGui import QFont, QColor, QBrush, QPixmap

class TableSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        horizontalHeader = ["编号", "姓名", "性别", "年龄", "职业"]

        table = QTableWidget()
        table.setColumnCount(5)
        table.setRowCount(2)
        table.setHorizontalHeaderLabels(horizontalHeader)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectColumns)
        table.setSelectionMode(QTableWidget.SingleSelection)

        for index in range(table.columnCount()):
            headItem = table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        table.setColumnWidth(4, 100)
        table.setRowHeight(0, 40)
        # self.table.setFrameShape(QFrame.HLine)#设定样式
        # self.table.setShowGrid(False) #取消网格线
        # self.table.verticalHeader().setVisible(False) #隐藏垂直表头

        table.setItem(0, 0, QTableWidgetItem("001"))
        table.setItem(0, 1, QTableWidgetItem("刘亦菲"))
        genderComb = QComboBox()
        genderComb.addItem("男")
        genderComb.addItem("女")
        genderComb.setCurrentIndex(1)
        table.setCellWidget(0, 2, genderComb)
        table.setItem(0, 3, QTableWidgetItem("30"))
        table.setItem(0, 4, QTableWidgetItem("演员"))

        table.setItem(1, 0, QTableWidgetItem("002"))
        table.setItem(1, 1, QTableWidgetItem("马云"))
        genderComb = QComboBox()
        genderComb.addItem("男")
        genderComb.addItem("女")
        genderComb.setCurrentIndex(0)
        table.setCellWidget(1, 2, genderComb)
        table.setItem(1, 3, QTableWidgetItem("50"))
        table.setItem(1, 4, QTableWidgetItem("企业家"))

        row_count = table.rowCount()
        table.insertRow(row_count)
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(table)
        self.setLayout(mainLayout)

        self.resize(600, 280)
        self.center()
        self.setWindowTitle("TableWidget Excempt")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = TableSheet()
    table.show()
    sys.exit(app.exec_())