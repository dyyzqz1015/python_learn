import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QInputDialog,QListWidgetItem
#导入Ui文件
from Qt5_python_GUI.CalldemoListWidgetOp.demoListWidgetOp import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow,QDialog):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.listWidget.addItem('Ice Cream')
        self.listWidget.addItem('Soda')
        self.listWidget.addItem('Coffee')
        self.listWidget.addItem('Chocolate')

        self.listWidget.addItems(['abd','dib','ddkw'])
        self.lineEdit.setText(str(self.listWidget.count()))

        # self.psuhButtonAdd.clicked.connect(self.Addlist)
        self.pushButtonEdit.clicked.connect(self.Editlist)
        self.pushButtonDelete.clicked.connect(self.Delitem)
        self.pushButtonDeleteAll.clicked.connect(self.DeleteAll)
        self.psuhButtonAdd.clicked.connect(self.Dispay)

    def Addlist(self):
        self.listWidget.addItem(self.lineEdit.text())


    def Editlist(self):
        row=self.listWidget.currentRow()
        newtext,ok=QInputDialog.getText(self,"Enter new text","Enter new text")
        if ok and (len(newtext)!=0):
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.listWidget.insertItem(row,QListWidgetItem(newtext))

    def Delitem(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def DeleteAll(self):
        self.listWidget.clear()

    def Dispay(self):
        self.lineEdit.setText(str(self.listWidget.currentRow()))
        self.listWidget.insertItem(self.listWidget.currentRow(),'插入')
        self.listWidget.insertItems(self.listWidget.currentRow(), ['插入1','插入2'])



if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())