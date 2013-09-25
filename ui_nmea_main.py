# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_nmea_main.ui'
#
# Created: Sun Sep 15 19:03:35 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_nmea_main(object):
    def setupUi(self, nmea_main):
        nmea_main.setObjectName(_fromUtf8("nmea_main"))
        nmea_main.setEnabled(True)
        nmea_main.resize(500, 75)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nmea_main.sizePolicy().hasHeightForWidth())
        nmea_main.setSizePolicy(sizePolicy)
        nmea_main.setMinimumSize(QtCore.QSize(500, 75))
        nmea_main.setMaximumSize(QtCore.QSize(500, 75))
        nmea_main.setMouseTracking(False)
        nmea_main.setAutoFillBackground(False)
        nmea_main.setSizeGripEnabled(False)
        self.widget = QtGui.QWidget(nmea_main)
        self.widget.setGeometry(QtCore.QRect(1, 10, 491, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addBut = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBut.sizePolicy().hasHeightForWidth())
        self.addBut.setSizePolicy(sizePolicy)
        self.addBut.setObjectName(_fromUtf8("addBut"))
        self.horizontalLayout.addWidget(self.addBut)
        self.settBut = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settBut.sizePolicy().hasHeightForWidth())
        self.settBut.setSizePolicy(sizePolicy)
        self.settBut.setObjectName(_fromUtf8("settBut"))
        self.horizontalLayout.addWidget(self.settBut)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.ButExit = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButExit.sizePolicy().hasHeightForWidth())
        self.ButExit.setSizePolicy(sizePolicy)
        self.ButExit.setObjectName(_fromUtf8("ButExit"))
        self.verticalLayout.addWidget(self.ButExit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(nmea_main)
        QtCore.QMetaObject.connectSlotsByName(nmea_main)

    def retranslateUi(self, nmea_main):
        nmea_main.setWindowTitle(_translate("nmea_main", "nmea_main", None))
        self.addBut.setText(_translate("nmea_main", "addLayer", None))
        self.settBut.setText(_translate("nmea_main", "NMEA sentences settings", None))
        self.pushButton.setText(_translate("nmea_main", "Browse", None))
        self.ButExit.setText(_translate("nmea_main", "cancel", None))

