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
        self.listWidget.setGeometry(QtCore.QRect(5, 11, 541, 521))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.projectNamer = QtWidgets.QLineEdit(self.frame_4)
        self.projectNamer.setGeometry(QtCore.QRect(70, 180, 361, 61))
        self.projectNamer.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.projectNamer.setText("")
        self.projectNamer.setObjectName("projectNamer")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 60, 361, 111))
        self.pushButton_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(70, 250, 371, 51))
        self.comboBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 320, 371, 51))
        self.comboBox_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.projectNamer_2 = QtWidgets.QLineEdit(self.frame_4)
        self.projectNamer_2.setGeometry(QtCore.QRect(70, 390, 361, 61))
        self.projectNamer_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.projectNamer_2.setText("")
        self.projectNamer_2.setObjectName("projectNamer_2")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 26))
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
        self.projectNamer.setPlaceholderText(_translate("MainWindow", "Enter Project Name"))
        self.pushButton_4.setText(_translate("MainWindow", "Create Project"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Python"))
        self.comboBox.setItemText(1, _translate("MainWindow", "C#"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ruby"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Web"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Flask"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "PyGame"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Django"))
        self.projectNamer_2.setPlaceholderText(_translate("MainWindow", "Enter Project Directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())