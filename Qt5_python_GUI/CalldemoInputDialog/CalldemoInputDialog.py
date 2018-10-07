import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog
#导入Ui文件
from Qt5_python_GUI.CalldemoInputDialog.demoInputDialog import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dispmessage)
    def dispmessage(self):
        countres=("Albania", "Algeria", "Andorra", "Angola",
                  "Antigua and Barbuda", "Argentina",
                  "Armenia", "Aruba","Australia", "Austria", "Azerbaijan")
        countryName,ok=QInputDialog.getItem(self,"Input Dialog",'List fo countries',countres,0,False)
        if ok and countres:
            self.lineEdit.setText(countryName)


if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())                   #循环显示