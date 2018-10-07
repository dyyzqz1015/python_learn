import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,\
    QTableWidgetItem,QHBoxLayout, QAbstractItemView,QComboBox

#导入Ui文件
from Qt5_python_GUI.CalldemoTableWidget.demoTableWidget import *

#继承UI父类Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()     #继承主类
        self.setupUi(self)

        # self.data=2
        # self.addcontent()
        # self.addItem()
        # self.initUI()
        self.addComboBox()

    # def addcontent(self):
    #     row=0
    #     for tup in self.data:
    #         col=0
    #
    #     col=2
    #     row=3
    #
    #
    #     for item in tup:
    #         oneitem=QTableWidgetItem(item)
    #         self.tableWidget.setItem(row,col,oneitem)
    #         col+=1
    #         row+=1
    #         data=[]
    #         data.append(('Suite','40'))
    #         data.append(('Super Luxury','30'))
    #         data.append(('Super Deluxe','20'))
    #         data.append(('Ordinary','10'))
    def addItem(self):
        for col in range(2):
            for row in range(3):
                oneitem=QTableWidgetItem('12')
                self.tableWidget.setItem(row,col,oneitem)

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(430, 230);
        conLayout = QHBoxLayout()
        # tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        conLayout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem("张三")
        self.tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        self.tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        self.tableWidget.setItem(0, 2, newItem)

        # 将表格变为禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置表格为整行选择
        self.tableWidget.setSelectionBehavior( QAbstractItemView.SelectRows)

        # 将行和列的大小设为与内容相匹配
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()

        # 表格表头的显示与隐藏
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setVisible(False)

        # 不显示表格单元格的分割线
        # self.tableWidget.setShowGrid(False)
        # 不显示垂直表头
        # self.tableWidget.verticalHeader().setVisible(False)

        self.setLayout(conLayout)



    def addComboBox(self):
        tabel=self.tableWidget
        tabel.setRowCount(4)
        tabel.setColumnCount(5)

        for row in range(4):
            for col in range(5):

                tabel.setItem(row,col,QTableWidgetItem(str(row)))
                comboBox = QComboBox()
                comboBox.addItems(['男','女'])
                tabel.setCellWidget(row,3,comboBox)




if __name__ == '__main__':
    app=QApplication(sys.argv)          #创建应用
    myWin=MyMainWindow()                #实例化应用
    qss_file = open('black_en.qss').read()
    myWin.setStyleSheet(qss_file)

    myWin.show()                        #显示应用
    exit(app.exec_())