#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py
import pegasus_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

import sys

class MainWindow(QtWidgets.QMainWindow, pegasus_window.Ui_MainWindow):

    def __init__(self):

        # Setting the UI to a class variable and connecting all GUI Components
        super(MainWindow, self).__init__()
        self.ui = pegasus_window.Ui_MainWindow()
        self.ui.setupUi(self)



def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Pegasus Motor Controller")
    window.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()