# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 191, 16))
        self.label.setObjectName("label")
        self.labelTest_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelTest_2.setGeometry(QtCore.QRect(10, 190, 271, 31))
        self.labelTest_2.setText("")
        self.labelTest_2.setObjectName("labelTest_2")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(10, 90, 256, 71))
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose the Diagnosis Tests"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("MainWindow", "Urine Analaysis $5"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("MainWindow", "Chest X Ray 100$"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("MainWindow", "Sugar Level test $3"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("MainWindow", "Hemoglobin test $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("MainWindow", "Thyroid Stimulating Harmone test $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)

