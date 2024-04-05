from uiV5 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


pyList = ["None", "Flask", "PyGame", "Django"]
rbList = ["None", "Gosu"]
csharpList = ["Console", "WPF"]
webList = ["HTML, CSS, JS"]
rustList = ["None"]
luaList = ["None"]

class Changer():
    def PythonChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(pyList)

    def RubyChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(rbList)

    def CsharpChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(csharpList)

        
    def WebChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(webList)

    def rustChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(rustList)

    def luaChanger(self):
        _translate = QtCore.QCoreApplication.translate
        self.libarySelect.clear()
        self.libarySelect.addItems(luaList)
        