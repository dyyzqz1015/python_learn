import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoMouseClick.demoMouseClick import *
from PyQt5.QtGui import QPainter

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.pos1=[0,0]
        self.pos2=[0,0]
    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        qp.drawLine(self.pos1[0],self.pos1[1],self.pos2[0],self.pos2[1])
        qp.end()

    def mousePressEvent(self, event):
        # if event.bottons() & QtCore.Qt.LeftButton:
            x=event.x()
            y=event.y()
            text="x:{0},y:{1}".format(x,y)
            self.labelPress.setText(text)

            # self.pos1[0],self.pos1[1]=event.pos().x(),event.pos().y()
    def mouseReleaseEvent(self, event):
        x=event.x()
        y=event.y()
        text="x:{0},y:{1}".format(x,y)
        self.labelRelease.setText(text)

        # self.pos2[0],self.pos2[1]=event.pos(),x(),event.pos().y()
        self.update()


if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())