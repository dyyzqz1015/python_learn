import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
#导入Ui文件
from Qt5_python_GUI.CalldemoFileDialog.demoFileDialog import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.openFileDialog)
        self.actionSave.triggered.connect(self.saveFileDialog)

    def openFileDialog(self):
        fname=QFileDialog.getOpenFileName(self,'Open file','d:/')

        if fname[0]:
            f=open(fname[0],'r')
            with f:
                data=f.read()
                self.textEdit.setText(data)
    def saveFileDialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog  #为什么要用|= 用意是什么

        #这里用下划线是什么用意
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        f = open(fileName,'w')
        text = self.textEdit.toPlainText()
        f.write(text)
        f.close()



if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    myWin.show()                        #显示应用
    exit(app.exec_())