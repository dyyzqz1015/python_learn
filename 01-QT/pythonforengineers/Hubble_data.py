#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/27 18:36
# @Author  : QinZai
# @File    : Hubble_data.py
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./data/hubble_data.csv')
print(data.head(0))
hear=['dist','rec_vel']
data_noheader=pd.read_csv('./data/hubble_data_no_headers.csv',names=hear)
print(data_noheader)

print(data_noheader['dist'])