import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Qt5_python_GUI.CalldemoCalculator.demoCalculator import *

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.pushButtonPlus.clicked.connect(self.Add)
        self.pushButtonSubtract.clicked.connect(self.Sub)
        self.pushButtonMultiply.clicked.connect(self.Multiply)
        self.pushButtonDivide.clicked.connect(self.Divide)

    def Add(self):
        if len(self.lineEditFirstNumber.text())!=0:
            a=int(self.lineEditFirstNumber.text())
        # else:
        #     a=0
        #
        if len(self.lineEditSecondNumber.text())!=0:
            b=int(self.lineEditSecondNumber.text())
        # else:
        #     b=0
            sum=a+b
        self.labelResult.setText("Addition:"+str(sum))
    def Sub(self):
        if len(self.lineEditFirstNumber.text())!=0:
            a=int(self.lineEditFirstNumber.text())
        # else:
        #     a=0

        if len(self.lineEditSecondNumber.text())!=0:
            b=int(self.lineEditSecondNumber.text())
        # else:
        #     b=0
            sum=a-b
        self.labelResult.setText("Substraction:"+str(sum))
    def Multiply(self):
        if len(self.lineEditFirstNumber.text())!=0:
            a=int(self.lineEditFirstNumber.text())
        # else:
        #     a=0

        if len(self.lineEditSecondNumber.text())!=0:
            b=int(self.lineEditSecondNumber.text())
        # else:
        #     b=0
            sum=a*b
        self.labelResult.setText("Multiplication:"+str(sum))
    def Divide(self):
        if len(self.lineEditFirstNumber.text())!=0:
            a=int(self.lineEditFirstNumber.text())
        # else:
        #     a=0
        #
        if len(self.lineEditSecondNumber.text())!=0:
            b=int(self.lineEditSecondNumber.text())
        # else:
        #     b=0
            sum=a/b
        self.labelResult.setText("Division:"+str(sum))









if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())