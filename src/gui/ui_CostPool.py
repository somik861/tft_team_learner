# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'CostPool.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_CostPool(object):
    def setupUi(self, CostPool):
        if not CostPool.objectName():
            CostPool.setObjectName(u"CostPool")
        CostPool.resize(386, 389)
        self.verticalLayout = QVBoxLayout(CostPool)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.costLayout = QHBoxLayout()
        self.costLayout.setObjectName(u"costLayout")
        self.label = QLabel(CostPool)
        self.label.setObjectName(u"label")

        self.costLayout.addWidget(self.label)

        self.costLabel = QLabel(CostPool)
        self.costLabel.setObjectName(u"costLabel")

        self.costLayout.addWidget(self.costLabel)

        self.costLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.costLayout)

        self.retranslateUi(CostPool)

        QMetaObject.connectSlotsByName(CostPool)
    # setupUi

    def retranslateUi(self, CostPool):
        CostPool.setWindowTitle(
            QCoreApplication.translate("CostPool", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "CostPool", u"Cost:", None))
        self.costLabel.setText(
            QCoreApplication.translate("CostPool", u"X", None))
    # retranslateUi
