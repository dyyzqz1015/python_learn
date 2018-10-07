import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoSpinner.demoSpinner import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.spinBoxBookQty.editingFinished.connect(self.result1)
        self.doubleSpinBoxSugarWeight.editingFinished.connect(self.result2)
    def result1(self):
        bookPrice=int(self.lineEditBookPrice_2.text())
        self.totalBookAmount=self.spinBoxBookQty.value()*bookPrice
        self.lineEditBookAmount_2.setText(str(self.totalBookAmount))
    def result2(self):
        bookPrice=int(self.lineEditSugarPrice.text())
        self.totalSugarAmount=self.doubleSpinBoxSugarWeight.value()*bookPrice
        self.lineEditSugarAmount.setText(str(self.totalSugarAmount))

        self.label_3.setText(str(self.totalSugarAmount+self.totalBookAmount))



if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())                   #循环显示