# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat Jan 12 23:48:29 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(868, 613)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchBar = QtGui.QLineEdit(self.centralwidget)
        self.searchBar.setMinimumSize(QtCore.QSize(0, 20))
        self.searchBar.setObjectName(_fromUtf8("searchBar"))
        self.gridLayout.addWidget(self.searchBar, 0, 0, 1, 1)
        self.searchBtn = QtGui.QPushButton(self.centralwidget)
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.gridLayout.addWidget(self.searchBtn, 0, 1, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setMaximumSize(QtCore.QSize(69, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.statusLbl = QtGui.QLabel(self.splitter)
        self.statusLbl.setMaximumSize(QtCore.QSize(74, 16777215))
        self.statusLbl.setText(_fromUtf8(""))
        self.statusLbl.setObjectName(_fromUtf8("statusLbl"))
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 2)
        self.downloadList = QtGui.QListWidget(self.centralwidget)
        self.downloadList.setMaximumSize(QtCore.QSize(16777215, 150))
        self.downloadList.setObjectName(_fromUtf8("downloadList"))
        self.gridLayout.addWidget(self.downloadList, 3, 0, 1, 2)
        self.songList = QtGui.QListWidget(self.centralwidget)
        self.songList.setObjectName(_fromUtf8("songList"))
        self.gridLayout.addWidget(self.songList, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchBtn.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "Downloads:", None))
        self.label_2.setText(_translate("MainWindow", "Login Status:", None))

