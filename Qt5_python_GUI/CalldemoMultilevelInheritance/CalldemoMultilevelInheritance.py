import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
#导入Ui文件
from Qt5_python_GUI.CalldemoMultilevelInheritance.demoMultilevelInheritance import *

class Student:
    name=''
    code=''
    def __init__(self,code,name):
        self.code=code
        self.name=name
    def getCode(self):
        return self.code
    def getName(self):
        return self.name

class Marks(Student):
    historyMarks=0
    geographyMarks=0
    def __init__(self,code,name,historyMarks,geographyMarks):
        Student.__init__(self,code,name)
        self.historyMarks=historyMarks
        self.geographyMarks=geographyMarks
    def getHistoryMarks(self):
        return self.historyMarks
    def getGeographyMarks(self):
        return self.geographyMarks
class Result(Marks):
    totalMarks=0
    percentage=0
    def __init__(self,code,name,historyMarks,geographyMarks):
        Marks.__init__(self,code,name,historyMarks,geographyMarks)
        self.totalMarks=historyMarks+geographyMarks
        self.percentage=(historyMarks+geographyMarks)/200*100
    def getTotalMarks(self):
        return self.totalMarks
    def getPercentage(self):
        return self.percentage



#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.ButtonClickMe.clicked.connect(self.dispmessage)

    def dispmessage(self):
        resultObj=Result(self.lineEditCode.text(),self.lineEditName.text(),int(self.lineEditHistoryMarks.text()),int(self.lineEditGeographyMarks.text()))
        self.lineEditTotal.setText(str(resultObj.getTotalMarks()))
        self.lineEditPercentage.setText(str(resultObj.getGeographyMarks()))



if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())                   #循环显示

mark=Marks('001','qinzai',19,29)
print(mark.getCode(),mark.getName(),mark.getHistoryMarks(),mark.getGeographyMarks())

result=Result('001','name',19,39)
print(result.getTotalMarks(),result.getPercentage())