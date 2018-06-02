#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/27 17:12
# @Author  : QinZai
# @File    : list_comp.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
def List():
    x = [5,10,15,20,25]
    #[ <do something> for value in list]
    y=[n/5 for n in x]

    print(x,y)
def SinCos():
    # Create x, evenly spaced between 0 to 20
    x = np.linspace(0, 20, 1000)        #平均从0~20，平均产生1000个数

    y1=np.sin(x)
    y2=np.cos(x)


    # Plot the sin and cos functions
    plt.plot(x , y1, "-g", label="sine")        #label设置 Y1标签为sine
    plt.plot(x , y2, "-b", label="cos")         #label设置 Y2标签为sine

    # # The legend should be in the top right corner
    plt.legend(loc="upper right")       #显示所有的标签



    # Limit the y axis to -1.5 to 1.5
    plt.ylim(-1.5, 1.5)     #y轴的范围
    plt.xlim(-20,30)        #x轴的范围
    plt.show()
def plt_bar():
    salary=np.fromfile('salaries.txt',dtype=int,sep=',')        #读取数字的文件
    print(salary)
    names=np.genfromtxt('names.txt',dtype='str',delimiter=',')      #读取文本的文件
    print(names)


    x = np.arange(len(names))

    plt.bar(x,salary)               #plt.bar是显示直方图，x是横坐标的值 ，salary是纵坐标的值
    plt.xticks(x,names)             #plt.xticks,将names替换x的作为刻度
    plt.ylabel("Salaries")          #plt.ylabel 标记纵轴的名称
    plt.xlabel("Names")             #plt.xlabel 标记横轴的名称
    plt.title("Salary of 10 random people")         #plt.title 图的标题
    plt.show()
