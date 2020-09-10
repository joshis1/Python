# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coredumputilframe.ui'
#
# Created: Thu Oct 22 09:57:00 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_coreDumpUtilFrame(object):
    def setupUi(self, coreDumpUtilFrame):
        coreDumpUtilFrame.setObjectName(_fromUtf8("coreDumpUtilFrame"))
        coreDumpUtilFrame.setWindowModality(QtCore.Qt.ApplicationModal)
        coreDumpUtilFrame.resize(655, 380)
        coreDumpUtilFrame.setMaximumSize(QtCore.QSize(655, 430))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        coreDumpUtilFrame.setFont(font)
        self.centralWidget = QtGui.QWidget(coreDumpUtilFrame)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lbanner = QtGui.QLabel(self.centralWidget)
        self.lbanner.setGeometry(QtCore.QRect(20, 0, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbanner.setFont(font)
        self.lbanner.setWordWrap(True)
        self.lbanner.setObjectName(_fromUtf8("lbanner"))
        self.lbannerImage = QtGui.QLabel(self.centralWidget)
        self.lbannerImage.setGeometry(QtCore.QRect(370, -10, 331, 81))
        self.lbannerImage.setText(_fromUtf8(""))
        self.lbannerImage.setPixmap(QtGui.QPixmap(_fromUtf8("LogoSJ.png")))
        self.lbannerImage.setObjectName(_fromUtf8("lbannerImage"))
        self.lArchitecture = QtGui.QLabel(self.centralWidget)
        self.lArchitecture.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.lArchitecture.setObjectName(_fromUtf8("lArchitecture"))
        self.comboArchType = QtGui.QComboBox(self.centralWidget)
        self.comboArchType.setGeometry(QtCore.QRect(290, 90, 77, 21))
        self.comboArchType.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboArchType.setObjectName(_fromUtf8("comboArchType"))
        self.comboArchType.addItem(_fromUtf8(""))
        self.comboArchType.addItem(_fromUtf8(""))
        self.lSysRoot = QtGui.QLabel(self.centralWidget)
        self.lSysRoot.setGeometry(QtCore.QRect(20, 140, 54, 15))
        self.lSysRoot.setObjectName(_fromUtf8("lSysRoot"))
        self.bSysRootBrowse = QtGui.QPushButton(self.centralWidget)
        self.bSysRootBrowse.setGeometry(QtCore.QRect(290, 130, 85, 27))
        self.bSysRootBrowse.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bSysRootBrowse.setObjectName(_fromUtf8("bSysRootBrowse"))
        self.lSysRootFilePath = QtGui.QLabel(self.centralWidget)
        self.lSysRootFilePath.setGeometry(QtCore.QRect(430, 130, 251, 16))
        self.lSysRootFilePath.setObjectName(_fromUtf8("lSysRootFilePath"))
        self.lApplicationExe = QtGui.QLabel(self.centralWidget)
        self.lApplicationExe.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.lApplicationExe.setObjectName(_fromUtf8("lApplicationExe"))
        self.bApplicationBrowser = QtGui.QPushButton(self.centralWidget)
        self.bApplicationBrowser.setGeometry(QtCore.QRect(290, 170, 85, 27))
        self.bApplicationBrowser.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bApplicationBrowser.setObjectName(_fromUtf8("bApplicationBrowser"))
        self.lApplicationFilePath = QtGui.QLabel(self.centralWidget)
        self.lApplicationFilePath.setGeometry(QtCore.QRect(430, 170, 101, 20))
        self.lApplicationFilePath.setObjectName(_fromUtf8("lApplicationFilePath"))
        self.lCoreFile = QtGui.QLabel(self.centralWidget)
        self.lCoreFile.setGeometry(QtCore.QRect(20, 220, 121, 16))
        self.lCoreFile.setObjectName(_fromUtf8("lCoreFile"))
        self.lCoreFileBrowser = QtGui.QPushButton(self.centralWidget)
        self.lCoreFileBrowser.setGeometry(QtCore.QRect(290, 210, 85, 27))
        self.lCoreFileBrowser.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lCoreFileBrowser.setStatusTip(_fromUtf8(""))
        self.lCoreFileBrowser.setObjectName(_fromUtf8("lCoreFileBrowser"))
        self.lCorefileBrowser = QtGui.QLabel(self.centralWidget)
        self.lCorefileBrowser.setGeometry(QtCore.QRect(430, 210, 101, 16))
        self.lCorefileBrowser.setObjectName(_fromUtf8("lCorefileBrowser"))
        self.bgetBackTrace = QtGui.QPushButton(self.centralWidget)
        self.bgetBackTrace.setGeometry(QtCore.QRect(160, 280, 231, 27))
        self.bgetBackTrace.setObjectName(_fromUtf8("bgetBackTrace"))
        coreDumpUtilFrame.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(coreDumpUtilFrame)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 655, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        coreDumpUtilFrame.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(coreDumpUtilFrame)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        coreDumpUtilFrame.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(coreDumpUtilFrame)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        coreDumpUtilFrame.setStatusBar(self.statusBar)

        self.retranslateUi(coreDumpUtilFrame)
        QtCore.QMetaObject.connectSlotsByName(coreDumpUtilFrame)
        coreDumpUtilFrame.setTabOrder(self.comboArchType, self.bSysRootBrowse)
        coreDumpUtilFrame.setTabOrder(self.bSysRootBrowse, self.bApplicationBrowser)
        coreDumpUtilFrame.setTabOrder(self.bApplicationBrowser, self.lCoreFileBrowser)
        coreDumpUtilFrame.setTabOrder(self.lCoreFileBrowser, self.bgetBackTrace)

    def retranslateUi(self, coreDumpUtilFrame):
        coreDumpUtilFrame.setWindowTitle(_translate("coreDumpUtilFrame", "XPlatform CoreDump Analysis Utility", None))
        self.lbanner.setText(_translate("coreDumpUtilFrame", "     Cross Platform CoreDump Analysis Utility", None))
        self.lArchitecture.setText(_translate("coreDumpUtilFrame", "  Architecture", None))
        self.comboArchType.setToolTip(_translate("coreDumpUtilFrame", "select the architecture", None))
        self.comboArchType.setItemText(0, _translate("coreDumpUtilFrame", "    MIPS", None))
        self.comboArchType.setItemText(1, _translate("coreDumpUtilFrame", "    X86", None))
        self.lSysRoot.setText(_translate("coreDumpUtilFrame", "SysRoot", None))
        self.bSysRootBrowse.setToolTip(_translate("coreDumpUtilFrame", "Give the Path of fileSystem  - fs in the path staging of the sandbox.", None))
        self.bSysRootBrowse.setText(_translate("coreDumpUtilFrame", "Browse...", None))
        self.lSysRootFilePath.setText(_translate("coreDumpUtilFrame", "No File Selected", None))
        self.lApplicationExe.setText(_translate("coreDumpUtilFrame", "Application-Exe", None))
        self.bApplicationBrowser.setToolTip(_translate("coreDumpUtilFrame", "Select the Application - Exe . The main binary - process.", None))
        self.bApplicationBrowser.setText(_translate("coreDumpUtilFrame", "Browse...", None))
        self.lApplicationFilePath.setText(_translate("coreDumpUtilFrame", "No File Selected", None))
        self.lCoreFile.setText(_translate("coreDumpUtilFrame", "Core-file ", None))
        self.lCoreFileBrowser.setToolTip(_translate("coreDumpUtilFrame", "Give the path of core file - this can be even compressed form like lzo.", None))
        self.lCoreFileBrowser.setText(_translate("coreDumpUtilFrame", "  Browse...", None))
        self.lCorefileBrowser.setText(_translate("coreDumpUtilFrame", "No File Selected", None))
        self.bgetBackTrace.setToolTip(_translate("coreDumpUtilFrame", "This will get the back trace, the backtrace log is stored in bt.txt", None))
        self.bgetBackTrace.setText(_translate("coreDumpUtilFrame", "Get BackTrace", None))

