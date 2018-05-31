import sys
from PyQt4.QtGui import QTreeWidgetItem, QMessageBox, QFileDialog
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from justExtract import justExtract

from export import exportData

__author__ = 'mudit'

import mainDialogModified
from PyQt4 import QtCore, QtGui


class justExtractThread(QtCore.QThread, justExtract):
    eventRowExtracted = pyqtSignal(list)

    def processRow(self, data):
        print data
        self.eventRowExtracted.emit([data])

    def run(self):
        self.extract()

    def startExtracting(self, url):
        self.setUrl(url)
        self.start()

    def stopExtracting(self):
        print "This called"
        self.terminate()


class MainWindow(QtGui.QDialog):
    signalStart = pyqtSignal(str)
    signalStop = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        # QtGui.QDialog.__init__(self)

        Ui = mainDialogModified.Ui_dialogMain()
        Ui.setupUi(self)
        self.Ui = Ui

    def getData(self):
        arr = []
        tree = self.Ui.treeWidget
        rootItem = tree.invisibleRootItem()
        child_count = rootItem.childCount()

        for x in range(child_count):
            item = rootItem.child(x)
            arr.append([str(item.text(0)), str(item.text(1)), str(item.text(2)), str(item.text(3))])

        return arr

    def exportClicked(self):
        filename = str(QFileDialog.getSaveFileName(self, "Save", "filename.csv"))
        if filename.strip() != '':
            data = self.getData()
            export = exportData(data)
            export.toCSV(filename.strip())
            QMessageBox.information(self, "Export", "Export Successful to CSV format at " + filename)

    def addRow(self, arr):
        rows = self.Ui.treeWidget.topLevelItemCount()
        col = 0
        for data in arr:
            print data
            self.Ui.treeWidget.addTopLevelItem(QTreeWidgetItem(data))

    def extractingFinished(self):
        QMessageBox.information(self, "Extracting Finished.",
                                "Extracting entries for link " + self.Ui.textUrl.text() + " finished")
        self.Ui.changeToEditMode()

    def grabClicked(self):

        if self.Ui.isStopMode == True:
            self.Ui.changeToEditMode()
            self.signalStop.emit()
        else:
            text = str(self.Ui.textUrl.text())
            text = text.strip()
            if text == '':
                QMessageBox.critical(self, "Enter valid url",
                                     "Please enter a valid url.")
                return

            self.Ui.changeToFixedMode()
            self.signalStart.emit(text)

    def clearTree(self):
        self.Ui.clearTree()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    test = justExtractThread()

    # Connecting signals and slot
    test.eventRowExtracted.connect(mainWindow.addRow)
    mainWindow.signalStart.connect(test.startExtracting)
    mainWindow.signalStop.connect(test.stopExtracting)
    test.finished.connect(mainWindow.extractingFinished)

    mainWindow.show()

    sys.exit(app.exec_())
