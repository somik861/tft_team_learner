# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'TeamSelection.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy,
                               QVBoxLayout, QWidget)

from src.gui.ChampionSlot import ChampionSlot


class Ui_TeamSelection(object):
    def setupUi(self, TeamSelection):
        if not TeamSelection.objectName():
            TeamSelection.setObjectName(u"TeamSelection")
        TeamSelection.resize(544, 271)
        TeamSelection.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(TeamSelection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row1Layout = QHBoxLayout()
        self.row1Layout.setSpacing(0)
        self.row1Layout.setObjectName(u"row1Layout")
        self.slot1 = ChampionSlot(TeamSelection)
        self.slot1.setObjectName(u"slot1")

        self.row1Layout.addWidget(self.slot1)

        self.slot2 = ChampionSlot(TeamSelection)
        self.slot2.setObjectName(u"slot2")

        self.row1Layout.addWidget(self.slot2)

        self.slot3 = ChampionSlot(TeamSelection)
        self.slot3.setObjectName(u"slot3")

        self.row1Layout.addWidget(self.slot3)

        self.slot4 = ChampionSlot(TeamSelection)
        self.slot4.setObjectName(u"slot4")

        self.row1Layout.addWidget(self.slot4)

        self.slot5 = ChampionSlot(TeamSelection)
        self.slot5.setObjectName(u"slot5")

        self.row1Layout.addWidget(self.slot5)

        self.verticalLayout.addLayout(self.row1Layout)

        self.row2Layout = QHBoxLayout()
        self.row2Layout.setSpacing(0)
        self.row2Layout.setObjectName(u"row2Layout")
        self.slot6 = ChampionSlot(TeamSelection)
        self.slot6.setObjectName(u"slot6")

        self.row2Layout.addWidget(self.slot6)

        self.slot7 = ChampionSlot(TeamSelection)
        self.slot7.setObjectName(u"slot7")

        self.row2Layout.addWidget(self.slot7)

        self.slot8 = ChampionSlot(TeamSelection)
        self.slot8.setObjectName(u"slot8")

        self.row2Layout.addWidget(self.slot8)

        self.slot9 = ChampionSlot(TeamSelection)
        self.slot9.setObjectName(u"slot9")

        self.row2Layout.addWidget(self.slot9)

        self.slot10 = ChampionSlot(TeamSelection)
        self.slot10.setObjectName(u"slot10")

        self.row2Layout.addWidget(self.slot10)

        self.verticalLayout.addLayout(self.row2Layout)

        self.retranslateUi(TeamSelection)

        QMetaObject.connectSlotsByName(TeamSelection)
    # setupUi

    def retranslateUi(self, TeamSelection):
        TeamSelection.setWindowTitle(
            QCoreApplication.translate("TeamSelection", u"Form", None))
    # retranslateUi
