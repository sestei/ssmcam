#!/usr/bin/env python

import subprocess
import shlex
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
        self.cmdRecHandles = [None] * 8
        self.cmdViewHandles = [None] * 8
        self.tmrCleanUp = QtCore.QTimer(self)
        self.tmrCleanUp.timeout.connect(self.cleanUpEvent)
        self.tmrCleanUp.start(1000)


    def viewCamera(self, idCam, startView):
        if startView:
            textCam = self.getCamDescription(idCam)
            cmd = self.config.view_cmd.format(idCam, textCam)
            cmd = shlex.split(cmd)
            self.cmdViewHandles[idCam-1] = subprocess.Popen(cmd, shell=False)
        else:
            handle = self.cmdViewHandles[idCam-1]
            if handle:
                handle.terminate()
            self.cmdViewHandles[idCam-1] = None
            

    def recordCamera(self, idCam, startRecording):
        if startRecording:
            dt = datetime.now()
            fname = dt.strftime('%Y%m%d-%Hh%Mm%Ss')
            fname += '_{0}'.format(self.getCamDescription(idCam))
            cmd = self.config.record_cmd.format(
                idCam,
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
        self.viewCamera(1, self.pbCam1.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam2_clicked(self):
        self.viewCamera(2, self.pbCam2.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam3_clicked(self):
        self.viewCamera(3, self.pbCam3.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam4_clicked(self):
        self.viewCamera(4, self.pbCam4.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam5_clicked(self):
        self.viewCamera(5, self.pbCam5.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam6_clicked(self):
        self.viewCamera(6, self.pbCam6.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam7_clicked(self):
        self.viewCamera(7, self.pbCam7.isChecked())

    @QtCore.pyqtSlot()
    def on_pbCam8_clicked(self):
        self.viewCamera(8, self.pbCam8.isChecked())

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


