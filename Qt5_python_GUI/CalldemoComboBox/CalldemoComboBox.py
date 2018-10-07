import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoComboBox.demoComboBox import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.label_2.setText("ComboBox:"+str(self.comboBox.count()))        #count的方法统计当前有多少个选项
        self.comboBox.activated.connect(self.dispay)                        #activated激活当前行选项，并显示
        self.pushButton.clicked.connect(self.addItem)                       #增加一个单项
        self.pushButton_2.clicked.connect(self.addItems)                    #增加多项
        self.pushButton_3.clicked.connect(self.removeItem)                  #移除一项
        self.comboBox.setEditable(True)                                     #设置选项为可编辑
        self.comboBox.setMaxCount(10)                                       #设置选项的最大数
        self.comboBox.setItemText(self.comboBox.currentIndex(),'abcd')      #获取当前的位置和编辑当前项

    def dispay(self):
        self.label_2.setText(self.comboBox.currentText())                   #currentText的方法获取当前的值

    def addItem(self):
        self.comboBox.addItem("增加一个项目")                              #增加单项
    def addItems(self):
        self.comboBox.addItems(["增加项目1","增加项目2"])                   #增加多项
    def removeItem(self):
        self.comboBox.removeItem(self.comboBox.currentIndex())              #移除当前项

if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())