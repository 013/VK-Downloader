# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon Jan 07 22:27:45 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(868, 614)
        self.songList = QtGui.QListWidget(Form)
        self.songList.setGeometry(QtCore.QRect(10, 48, 681, 551))
        self.songList.setObjectName(_fromUtf8("songList"))
        self.statusLblNU = QtGui.QLabel(Form)
        self.statusLblNU.setGeometry(QtCore.QRect(700, 0, 41, 41))
        self.statusLblNU.setObjectName(_fromUtf8("statusLblNU"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 50, 151, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.loginBtn = QtGui.QPushButton(self.layoutWidget)
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.verticalLayout.addWidget(self.loginBtn)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 681, 25))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchBtn = QtGui.QPushButton(self.layoutWidget_2)
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.horizontalLayout.addWidget(self.searchBtn)
        self.statusLbl = QtGui.QLabel(Form)
        self.statusLbl.setGeometry(QtCore.QRect(740, 0, 121, 41))
        self.statusLbl.setText(_fromUtf8(""))
        self.statusLbl.setObjectName(_fromUtf8("statusLbl"))
        self.currentLbl = QtGui.QLabel(Form)
        self.currentLbl.setGeometry(QtCore.QRect(700, 190, 161, 41))
        self.currentLbl.setText(_fromUtf8(""))
        self.currentLbl.setScaledContents(False)
        self.currentLbl.setObjectName(_fromUtf8("currentLbl"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "VK.com Downloader 3000", None))
        self.statusLblNU.setText(_translate("Form", "Status:", None))
        self.loginBtn.setText(_translate("Form", "Login", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "Search query", None))
        self.searchBtn.setText(_translate("Form", "Search", None))

