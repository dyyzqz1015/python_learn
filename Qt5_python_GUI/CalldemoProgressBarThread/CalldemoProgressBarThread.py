import sys
import threading
import time
from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoProgressBarThread.demoProgressBarThread import *


 #继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


class myThread(threading.Thread):
#
    conuter=0
    def __init__(self,w):
        threading.Thread.__init__(self)
        self.w=w

        self.conuter=0
    def run(self):
        print("Starting"+self.name)
        while self.conuter<=100:
            time.sleep(1)

            self.w.ui.progressBar.setValue(self.conuter)
            self.conuter+=10
            print("Exiting "+self.name)





if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    thread1=myThread(myWin)
    thread1.start()
    myWin.exec()
    # myWin.show()                        #显示应用
    # exit(app.exec_())
    sys.exit(app.exec_())