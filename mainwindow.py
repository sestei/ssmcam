#!/usr/bin/env python

import subprocess
from PyQt4 import QtGui,QtCore
from config import Config
import uiCameras

class MainWindow(QtGui.QDialog, uiCameras.Ui_CamDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.config = Config()
        self.updateFromConfig()

    def activateCamera(self, idCam):
        textCam = self.getCamDescription(idCam)
        cmd = self.config.action_cmd.format(idCam, textCam)
        subprocess.Popen(cmd, shell=True)

    def getCamDescription(self, idCam):
        handle = getattr(self,'txtDesc{0}'.format(idCam))
        return str(handle.text())

    def updateConfig(self):
        for ii in range(0,8):
            self.config.descriptions[ii] = self.getCamDescription(ii+1)

            handle = getattr(self,'chkCam{0}'.format(ii+1))
            self.config.enabled[ii] = handle.isChecked()

    def updateFromConfig(self):
        for ii in range(0,8):
            handle = getattr(self,'txtDesc{0}'.format(ii+1))
            handle.setText(self.config.descriptions[ii])

            handle = getattr(self,'chkCam{0}'.format(ii+1))
            handle.setChecked(self.config.enabled[ii])

    # ==== SLOTS ====

    def closeEvent(self,ev):
        self.updateConfig()
        self.config.saveToFile()
        super(MainWindow,self).closeEvent(ev)

    @QtCore.pyqtSlot()
    def on_pbCam1_clicked(self):
        self.activateCamera(1)

    @QtCore.pyqtSlot()
    def on_pbCam2_clicked(self):
        self.activateCamera(2)

    @QtCore.pyqtSlot()
    def on_pbCam3_clicked(self):
        self.activateCamera(3)

    @QtCore.pyqtSlot()
    def on_pbCam4_clicked(self):
        self.activateCamera(4)

    @QtCore.pyqtSlot()
    def on_pbCam5_clicked(self):
        self.activateCamera(5)

    @QtCore.pyqtSlot()
    def on_pbCam6_clicked(self):
        self.activateCamera(6)

    @QtCore.pyqtSlot()
    def on_pbCam7_clicked(self):
        self.activateCamera(7)

    @QtCore.pyqtSlot()
    def on_pbCam8_clicked(self):
        self.activateCamera(8)
