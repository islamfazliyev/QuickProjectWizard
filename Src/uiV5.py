# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 91, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/images/Logo.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(330, 10, 571, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Viner Hand ITC\";\n"
"")
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.listWidget = QtWidgets.QListWidget(self.frame_5)
        self.listWidget.setGeometry(QtCore.QRect(5, 51, 541, 481))
        self.listWidget.setObjectName("listWidget")
        self.searchBar = QtWidgets.QLineEdit(self.frame_5)
        self.searchBar.setGeometry(QtCore.QRect(0, 10, 351, 31))
        self.searchBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchBar.setObjectName("searchBar")
        self.deleteItem = QtWidgets.QPushButton(self.frame_5)
        self.deleteItem.setGeometry(QtCore.QRect(360, 12, 31, 31))
        self.deleteItem.setObjectName("deleteItem")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.projectNamer = QtWidgets.QLineEdit(self.frame_4)
        self.projectNamer.setGeometry(QtCore.QRect(70, 180, 361, 61))
        self.projectNamer.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.projectNamer.setText("")
        self.projectNamer.setObjectName("projectNamer")
        self.createProject = QtWidgets.QPushButton(self.frame_4)
        self.createProject.setGeometry(QtCore.QRect(70, 60, 361, 111))
        self.createProject.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.createProject.setObjectName("createProject")
        self.langSelect = QtWidgets.QComboBox(self.frame_4)
        self.langSelect.setGeometry(QtCore.QRect(70, 250, 361, 51))
        self.langSelect.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.langSelect.setObjectName("langSelect")
        self.langSelect.addItem("")
        self.langSelect.addItem("")
        self.langSelect.addItem("")
        self.langSelect.addItem("")
        self.libarySelect = QtWidgets.QComboBox(self.frame_4)
        self.libarySelect.setGeometry(QtCore.QRect(70, 320, 361, 51))
        self.libarySelect.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.libarySelect.setObjectName("libarySelect")
        self.libarySelect.addItem("")
        self.libarySelect.addItem("")
        self.libarySelect.addItem("")
        self.libarySelect.addItem("")
        self.directoryAssign = QtWidgets.QLineEdit(self.frame_4)
        self.directoryAssign.setGeometry(QtCore.QRect(70, 390, 241, 61))
        self.directoryAssign.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.directoryAssign.setText("")
        self.directoryAssign.setObjectName("directoryAssign")
        self.selectFolder = QtWidgets.QPushButton(self.frame_4)
        self.selectFolder.setGeometry(QtCore.QRect(320, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectFolder.setFont(font)
        self.selectFolder.setStyleSheet("color: rgba(255,255,255, 1);")
        self.selectFolder.setObjectName("selectFolder")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Quick Project Wizard"))
        self.deleteItem.setText(_translate("MainWindow", "❌"))
        self.projectNamer.setPlaceholderText(_translate("MainWindow", "Enter Project Name"))
        self.createProject.setText(_translate("MainWindow", "Create Project"))
        self.langSelect.setItemText(0, _translate("MainWindow", "Python"))
        self.langSelect.setItemText(1, _translate("MainWindow", "C#"))
        self.langSelect.setItemText(2, _translate("MainWindow", "Ruby"))
        self.langSelect.setItemText(3, _translate("MainWindow", "Web"))
        self.libarySelect.setItemText(0, _translate("MainWindow", "None"))
        self.libarySelect.setItemText(1, _translate("MainWindow", "Flask"))
        self.libarySelect.setItemText(2, _translate("MainWindow", "PyGame"))
        self.libarySelect.setItemText(3, _translate("MainWindow", "Django"))
        self.directoryAssign.setPlaceholderText(_translate("MainWindow", "Enter Project Directory"))
        self.selectFolder.setText(_translate("MainWindow", "Select Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
