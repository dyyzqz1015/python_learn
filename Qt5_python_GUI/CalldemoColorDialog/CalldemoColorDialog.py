import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QColorDialog
#导入Ui文件
from Qt5_python_GUI.CalldemoColorDialog.demoColorDialog import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)
        # col=QColorDialog.getColor()
        # self.frameColor.setStyleSheet("QtWidget{background-color:%s}" % col.name())
        self.pushButtonColor.clicked.connect(self.dispcolor)
    def dispcolor(self):
        col=QColorDialog.getColor()
        if col.isValid():
            self.frameColor.setStyleSheet("QtWidget{background-color:%s}" % col.name())
            self.labelColor.setText("Your have selected the color"+str(col.name()))
if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())