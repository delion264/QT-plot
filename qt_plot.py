from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import sys  
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        
        self.N = 1001
        self.x = np.linspace(0, 2*np.pi, self.N)  # 100 time points
        self.y = np.sin(4*np.pi*self.x)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = np.delete(self.x, 0)  # Remove the first y element.
        self.x = np.append(self.x, self.x[-2] + 2*np.pi/(self.N))  # Add a new value 1 higher than the last.

        self.y = np.delete(self.y, 0) # Remove the first
        self.y = np.append(self.y, np.sin(4*np.pi*self.x[-1]))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

app = QtWidgets.QApplication(sys.argv) # sys.argv === command line args
w = MainWindow()
w.show()
sys.exit(app.exec_())
