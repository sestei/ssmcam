#!/usr/bin/env python

import subprocess
from datetime import datetime
from PyQt4 import QtGui,QtCore
from config import Config
import uiCameras

class MainWindow(QtGui.QDialog, uiCameras.Ui_CamDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.config = Config()
        self.updateFromConfig()
        self.cmdHandles = [None] * 8

    def activateCamera(self, idCam):
        textCam = self.getCamDescription(idCam)
        cmd = self.config.action_cmd.format(idCam, textCam)
        subprocess.Popen(cmd, shell=True)

    def recordCamera(self, idCam, startRecording):
        if startRecording:
            dt = datetime.now()
            fname = dt.strftime('%Y%m%d-%Hh%Mm%Ss')
            fname += '_{0}'.format(self.getCamDescription(idCam))
            cmd = self.config.record_cmd.format(
                idCam, self.getCamDescription(idCam), fname
            )
            self.cmdHandles[idCam-1] = subprocess.Popen(cmd, shell=False)
        else:
            handle = self.cmdHandles[idCam-1]
            if not handle:
                print "No handle found?!"
            print "sending terminate"
            handle.terminate()

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

    @QtCore.pyqtSlot()
    def on_pbRecord1_clicked(self):
        self.recordCamera(1, self.pbRecord1.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord2_clicked(self):
        self.recordCamera(2, self.pbRecord2.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord3_clicked(self):
        self.recordCamera(3, self.pbRecord3.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord4_clicked(self):
        self.recordCamera(4, self.pbRecord4.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord5_clicked(self):
        self.recordCamera(5, self.pbRecord5.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord6_clicked(self):
        self.recordCamera(6, self.pbRecord6.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord7_clicked(self):
        self.recordCamera(7, self.pbRecord7.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord8_clicked(self):
        self.recordCamera(8, self.pbRecord8.isChecked())


