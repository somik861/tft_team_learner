# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ChampionSlot.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_ChamionSlot(object):
    def setupUi(self, ChamionSlot):
        if not ChamionSlot.objectName():
            ChamionSlot.setObjectName(u"ChamionSlot")
        ChamionSlot.resize(523, 420)
        self.verticalLayout = QVBoxLayout(ChamionSlot)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(ChamionSlot)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(75, 75))
        self.label.setFrameShape(QFrame.Shape.WinPanel)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(ChamionSlot)

        QMetaObject.connectSlotsByName(ChamionSlot)
    # setupUi

    def retranslateUi(self, ChamionSlot):
        ChamionSlot.setWindowTitle(
            QCoreApplication.translate("ChamionSlot", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "ChamionSlot", u"Empty", None))
    # retranslateUi
