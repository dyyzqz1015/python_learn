import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CallListWidget3.demoListWidget3 import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.pushButtonAdd.clicked.connect(self.addlist)

    def addlist(self):
        self.listWidgetSelectedItems.addItem(self.lineEditFoodItem.text())
        self.lineEditFoodItem.setText("")
        self.lineEditFoodItem.setFocus()


if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())