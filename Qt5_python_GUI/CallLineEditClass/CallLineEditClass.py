import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CallLineEditClass.LineEditClass import *

class Student:
    name=""
    def __init__(self,name):
        self.name=name
    def printName(self):
        return self.name

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.pushButton.clicked.connect(self.dispmessage)

    def dispmessage(self):
        StudentObj=Student(self.lineEdit.text())
        self.label_2.setText("Hello "+StudentObj.printName())


if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())                   #循环显示