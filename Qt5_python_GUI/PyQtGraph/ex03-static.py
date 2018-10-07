import pyqtgraph as pg
import numpy as np

# x=np.random.normal(size=1000)
# y=np.random.normal(size=1000)
# pg.plot(x,y,pen=None,symbol='o')
x=np.random.random(10)
y=np.random.random(10)
pg.plot(x,y)

pg.QtGui.QGuiApplication.exec_()