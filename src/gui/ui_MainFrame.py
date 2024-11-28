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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MainFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(MainFrame)

        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate(
            "MainFrame", u"TFT Team Learner", None))
        self.label.setText(QCoreApplication.translate(
            "MainFrame", u"Hello world", None))
    # retranslateUi
