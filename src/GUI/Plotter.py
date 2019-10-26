#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqtgraph as pg
import numpy as np

class CustomWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('pyqtgraph example: Scrolling Plots')
        self.p = self.addPlot(labels =  {'left':'Position', 'bottom':'Time'})
        self.data = np.zeros(10)
        self.curve = self.p.plot(self.data, pen='b')

if __name__ == '__main__':
    w = CustomWidget()
    w.show()