# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created: Mon Jan 07 22:27:47 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(367, 67)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.username = QtGui.QLineEdit(Dialog)
        self.username.setStyleSheet(_fromUtf8("background-color: white;"))
        self.username.setInputMask(_fromUtf8(""))
        self.username.setText(_fromUtf8(""))
        self.username.setFrame(True)
        self.username.setObjectName(_fromUtf8("username"))
        self.horizontalLayout.addWidget(self.username)
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setStyleSheet(_fromUtf8(""))
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout.addWidget(self.password)
        self.login = QtGui.QPushButton(Dialog)
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout.addWidget(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.username.setPlaceholderText(_translate("Dialog", "Username", None))
        self.password.setPlaceholderText(_translate("Dialog", "Password", None))
        self.login.setText(_translate("Dialog", "Login", None))

