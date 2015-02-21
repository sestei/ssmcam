#!/usr/bin/env python

import subprocess
import shlex
from datetime import datetime
from PyQt4 import QtGui,QtCore
from config import Config
import uiCameras
        
def rotmethod(rotate):
    if rotate:
        return "rotate-180"
    else:
        return "none"

class MainWindow(QtGui.QDialog, uiCameras.Ui_CamDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.config = Config()
        self.updateFromConfig()
        self.cmdRecHandles = [None] * 5 
        self.cmdViewHandles = [None] * 5
        self.tmrCleanUp = QtCore.QTimer(self)
        self.tmrCleanUp.timeout.connect(self.cleanUpEvent)
        self.tmrCleanUp.start(1000)

    def viewCamera(self, idCam, startView, rotate=False):
        if startView:
            textCam = self.getCamDescription(idCam)
            cmd = self.config.view_cmd.format(
                idCam,
                rotmethod(rotate),
                textCam
            )
            cmd = shlex.split(cmd)
            self.cmdViewHandles[idCam-1] = subprocess.Popen(cmd, shell=False)
        else:
            handle = self.cmdViewHandles[idCam-1]
            if handle:
                handle.terminate()
            self.cmdViewHandles[idCam-1] = None
            

    def recordCamera(self, idCam, startRecording, rotate):
        if startRecording:
            dt = datetime.now()
            fname = dt.strftime('%Y%m%d-%Hh%Mm%Ss')
            fname += '_{0}'.format(self.getCamDescription(idCam))
            cmd = self.config.record_cmd.format(
                idCam,
                rotmethod(rotate),
                self.getCamDescription(idCam),
                fname
            )
            cmd = shlex.split(cmd)
            self.cmdRecHandles[idCam-1] = subprocess.Popen(cmd, shell=False)
        else:
            handle = self.cmdRecHandles[idCam-1]
            if handle:
                handle.terminate()
            self.cmdRecHandles[idCam-1] = None

    def getCamDescription(self, idCam):
        handle = getattr(self,'txtDesc{0}'.format(idCam))
        return str(handle.text())

    def updateConfig(self):
        for ii in range(0,5):
            self.config.descriptions[ii] = self.getCamDescription(ii+1)

            handle = getattr(self,'chkCam{0}'.format(ii+1))
            self.config.enabled[ii] = handle.isChecked()

            handle = getattr(self,'pbRotate{0}'.format(ii+1))
            self.config.rotate[ii] = handle.isChecked()

    def updateFromConfig(self):
        for ii in range(0,5):
            handle = getattr(self,'txtDesc{0}'.format(ii+1))
            handle.setText(self.config.descriptions[ii])

            handle = getattr(self,'chkCam{0}'.format(ii+1))
            handle.setChecked(self.config.enabled[ii])

            handle = getattr(self,'pbRotate{0}'.format(ii+1))
            handle.setChecked(self.config.rotate[ii])

    # ==== SLOTS ====

    def closeEvent(self,ev):
        self.updateConfig()
        self.config.saveToFile()
        super(MainWindow,self).closeEvent(ev)

    def cleanUpEvent(self):
        """
        checks for terminated child processes and resets respective buttons
        """
        for ii, handle in enumerate(self.cmdRecHandles):
            if handle and handle.poll() is not None:
                print "Recording process for camera {0} has terminated".format(ii+1)
                pb = getattr(self,'pbRecord{0}'.format(ii+1))
                pb.setChecked(False)
                self.cmdRecHandles[ii] = None
        for ii, handle in enumerate(self.cmdViewHandles):
            if handle and handle.poll() is not None:
                print "Live view process for camera {0} has terminated".format(ii+1)
                pb = getattr(self,'pbCam{0}'.format(ii+1))
                pb.setChecked(False)
                self.cmdViewHandles[ii] = None

    @QtCore.pyqtSlot()
    def on_pbCam1_clicked(self):
        self.viewCamera(1, self.pbCam1.isChecked(), self.pbRotate1.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam2_clicked(self):
        self.viewCamera(2, self.pbCam2.isChecked(), self.pbRotate2.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam3_clicked(self):
        self.viewCamera(3, self.pbCam3.isChecked(), self.pbRotate3.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam4_clicked(self):
        self.viewCamera(4, self.pbCam4.isChecked(), self.pbRotate4.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam5_clicked(self):
        self.viewCamera(5, self.pbCam5.isChecked(), self.pbRotate5.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord1_clicked(self):
        self.recordCamera(1, self.pbRecord1.isChecked(), self.pbRotate1.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord2_clicked(self):
        self.recordCamera(2, self.pbRecord2.isChecked(), self.pbRotate2.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord3_clicked(self):
        self.recordCamera(3, self.pbRecord3.isChecked(), self.pbRotate3.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord4_clicked(self):
        self.recordCamera(4, self.pbRecord4.isChecked(), self.pbRotate4.isChecked())

    @QtCore.pyqtSlot()
    def on_pbRecord5_clicked(self):
        self.recordCamera(5, self.pbRecord5.isChecked(), self.pbRotate5.isChecked())

    