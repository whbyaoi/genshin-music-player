import os
import sys
import time
from functools import partial

import pykeyboard
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QApplication, QStyleFactory, QListWidgetItem
from sheetDecomposer import sheetDecomposer
from playThread import playThread
from main_ui import Ui_Form


class mainWindow(Ui_Form, QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.sheetDir = os.getcwd() + '/sheets'
        self.sheetDec = sheetDecomposer()
        self.keyboardUnit = pykeyboard.PyKeyboard()
        self.playThread = None

        files = os.listdir(self.sheetDir)
        for file in files:
            item = QListWidgetItem(file)
            self.listWidget.insertItem(0, item)

        self.pushButton.clicked.connect(lambda: self.play(self.listWidget.currentItem().text()))

    @Slot(str)
    def play(self, name: str):
        self.sheetDec.load(name)
        time.sleep(5)
        self.playThread = playThread(self.sheetDec.sheet, 100)
        self.playThread.endSignal.connect(self.stop)
        self.playThread.start()
        self.pushButton.setEnabled(False)

    @Slot()
    def stop(self):
        self.pushButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
