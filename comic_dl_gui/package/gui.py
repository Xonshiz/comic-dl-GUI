# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1119, 877)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui_images/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.SpanningRole, spacerItem)
        self.urlLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName(_fromUtf8("urlLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.urlLabel)
        self.urlInputField = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlInputField.sizePolicy().hasHeightForWidth())
        self.urlInputField.setSizePolicy(sizePolicy)
        self.urlInputField.setObjectName(_fromUtf8("urlInputField"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.urlInputField)
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.downloadButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtGui.QFormLayout.SpanningRole, spacerItem1)
        self.textArea = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.textArea.sizePolicy().hasHeightForWidth())
        self.textArea.setSizePolicy(sizePolicy)
        self.textArea.setObjectName(_fromUtf8("textArea"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.textArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionReport_Issue = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui_images/Report Issue.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_Issue.setIcon(icon1)
        self.actionReport_Issue.setObjectName(_fromUtf8("actionReport_Issue"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui_images/Exit_Button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionReport_Issue_2 = QtGui.QAction(MainWindow)
        self.actionReport_Issue_2.setEnabled(True)
        self.actionReport_Issue_2.setIcon(icon1)
        self.actionReport_Issue_2.setObjectName(_fromUtf8("actionReport_Issue_2"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setIcon(icon2)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReport_Issue)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionReport_Issue_2)
        self.toolBar.addAction(self.actionExit_2)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionExit_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Comc-dl GUI", None))
        self.urlLabel.setText(_translate("MainWindow", "URL :", None))
        self.downloadButton.setText(_translate("MainWindow", "Download", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionReport_Issue.setText(_translate("MainWindow", "Report Issue", None))
        self.actionReport_Issue.setStatusTip(_translate("MainWindow", "Report an Issue on Github", None))
        self.actionReport_Issue.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit this application", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionReport_Issue_2.setText(_translate("MainWindow", "Report Issue", None))
        self.actionReport_Issue_2.setToolTip(_translate("MainWindow", "Report Issue on Github", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setToolTip(_translate("MainWindow", "Exit the application", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

