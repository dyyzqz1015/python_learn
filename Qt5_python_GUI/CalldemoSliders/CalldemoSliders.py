import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoSpinner.demoSliders import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrollhorizontal)
        self.verticalScrollBarPulseRate.valueChanged.connect(self.scrollhorizontal)
        self.horizontalSliderBloodPressure.valueChanged.connect(self.scrollhorizontal)
        self.verticalSliderCholestrolLevel.valueChanged.connect(self.scrollhorizontal)
    def scrollhorizontal(self,value):
        self.lineEditResult.setText("Sugar Level:"+str(value))
if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())