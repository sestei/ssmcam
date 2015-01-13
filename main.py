#!/usr/bin/python

import sys
from mainwindow import MainWindow
from PyQt4 import QtGui

print """
-=[ SSM CAM - Python & Qt based interface for Raspi cameras ]=-
          written by Sebastian Steinlechner, 2015
"""
qApp = QtGui.QApplication(sys.argv) 
Window = MainWindow()
Window.show()
qApp.exec_()