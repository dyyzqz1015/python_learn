import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CallListWidget.demoListWidget import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.listWidgetDiagnosis.itemClicked.connect(self.dispSelectedTest)

    def dispSelectedTest(self):
        self.labelTest_2.setText("You have selected"+self.listWidgetDiagnosis.currentItem().text())

if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())