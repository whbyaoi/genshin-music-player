# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
                               QSpinBox, QVBoxLayout, QWidget, QDoubleSpinBox, QTextBrowser)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 300)
        self.mainHorizontalLayout = QHBoxLayout(Form)
        self.mainHorizontalLayout.setContentsMargins(10, 10, 10, 10)

        self.leftWidget = QWidget(Form)
        self.verticalLayout = QVBoxLayout(self.leftWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.verticalLayout.addWidget(self.groupBox)

        self.widget = QWidget(Form)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QPushButton(self.widget)
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton2 = QPushButton(self.widget)
        self.pushButton2.setText('试听')
        self.horizontalLayout.addWidget(self.pushButton2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.mainHorizontalLayout.addWidget(self.leftWidget)

        self.textBrowser = QTextBrowser()
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setUndoRedoEnabled(True)
        self.textBrowser.setWordWrapMode(PySide6.QtGui.QTextOption.WrapMode.NoWrap)
        self.mainHorizontalLayout.addWidget(self.textBrowser)

        self.mainHorizontalLayout.setStretch(0, 1)
        self.mainHorizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Genshin Music Player", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u4e50\u8c31\u5217\u8868", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
    # retranslateUi
