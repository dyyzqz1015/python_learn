import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoLCD.demoLCD import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        timer=QtCore.QTimer(self)
        timer.timeout.connect(self.showLCD)
        timer.start(19)

    def showLCD(self):
        time=QtCore.QTime.currentTime()         #获取了当前的时间
        text=time.toString('hh:mm:ss')             #将时间进行格式化
        self.lcdNumber.display(text)            #显示到界面

if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())                   #循环显示