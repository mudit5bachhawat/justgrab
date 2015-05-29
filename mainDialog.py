# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created: Fri May 29 06:51:34 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialogMain(object):
    def setupUi(self, dialogMain):
        dialogMain.setObjectName(_fromUtf8("dialogMain"))
        dialogMain.resize(643, 381)
        dialogMain.setWindowOpacity(1.0)
        dialogMain.setToolTip(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(dialogMain)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonGrab = QtGui.QPushButton(dialogMain)
        self.buttonGrab.setObjectName(_fromUtf8("buttonGrab"))
        self.gridLayout.addWidget(self.buttonGrab, 0, 1, 1, 1)
        self.textUrl = QtGui.QLineEdit(dialogMain)
        self.textUrl.setObjectName(_fromUtf8("textUrl"))
        self.gridLayout.addWidget(self.textUrl, 0, 0, 1, 1)
        self.buttonExport = QtGui.QPushButton(dialogMain)
        self.buttonExport.setObjectName(_fromUtf8("buttonExport"))
        self.gridLayout.addWidget(self.buttonExport, 2, 1, 1, 1)
        self.line = QtGui.QFrame(dialogMain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.treeWidget = QtGui.QTreeWidget(dialogMain)
        self.treeWidget.setColumnCount(0)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.gridLayout.addWidget(self.treeWidget, 2, 0, 3, 1)
        self.labelStatus = QtGui.QLabel(dialogMain)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout.addWidget(self.labelStatus, 4, 1, 1, 1)
        self.buttonClear = QtGui.QPushButton(dialogMain)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.gridLayout.addWidget(self.buttonClear, 3, 1, 1, 1)

        self.retranslateUi(dialogMain)
        QtCore.QObject.connect(self.buttonGrab, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogMain.grabClicked)
        QtCore.QObject.connect(self.textUrl, QtCore.SIGNAL(_fromUtf8("returnPressed()")), dialogMain.grabClicked)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogMain.clearTree)
        QtCore.QObject.connect(self.buttonExport, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogMain.exportClicked)
        QtCore.QMetaObject.connectSlotsByName(dialogMain)

    def retranslateUi(self, dialogMain):
        dialogMain.setWindowTitle(_translate("dialogMain", "justGrab", None))
        self.buttonGrab.setText(_translate("dialogMain", "Grab", None))
        self.textUrl.setPlaceholderText(_translate("dialogMain", "Enter URL here eg: http://www.justdial.com/Mumbai/1-Star-Hotels/ct-333935", None))
        self.buttonExport.setText(_translate("dialogMain", "Export", None))
        self.buttonClear.setText(_translate("dialogMain", "Clear", None))

