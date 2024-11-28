# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'MainFrame.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget)

from src.gui.ChampionPool import ChampionPool
from src.gui.TeamSelection import TeamSelection


class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(646, 432)
        self.verticalLayout = QVBoxLayout(MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = TeamSelection(MainFrame)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(MainFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(MainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = ChampionPool()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 626, 397))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(MainFrame)

        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate(
            "MainFrame", u"TFT Team Learner", None))
    # retranslateUi
