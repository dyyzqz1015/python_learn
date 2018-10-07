import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CallMenuBar.demoMenuBar import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)


        self.toDraw=""
        self.actionDraw_Circle.triggered.connect(self.drawCircle)
        self.actionDraw_Rectangle.triggered.connect(self.drawRectangle)
        self.actionDraw_Line.triggered.connect(self.drawLine)
        self.actionPage_Setup.triggered.connect(self.pageSetup)
        self.actionSet_Password.triggered.connect(self.setPassword)
        self.actionCut.triggered.connect(self.cutMethod)
        self.actionCopy.triggered.connect(self.copyMethod)
        self.actionPaste.triggered.connect(self.pasteMethod)

    def drawCircle(self):
       self.label.setText("circle")
    def drawRectangle(self):
       self.label.setText("Rectangle")
    def drawLine(self):
       self.label.setText("Line")
    def pageSetup(self):
       self.label.setText("Page Setup menu item is selected")
    def setPassword(self):
       self.label.setText("setPassword")
    def cutMethod(self):
       self.label.setText("cut")
    def copyMethod(self):
       self.label.setText("copy")
    def pasteMethod(self):
       self.label.setText("paste")


if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())