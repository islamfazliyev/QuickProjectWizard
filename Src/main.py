import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidgetItem, QPushButton, QMessageBox, QComboBox
from uiV5 import Ui_MainWindow
from tinydb import TinyDB, Query
import subprocess
import shutil
from LibaryChanger import Changer
from creator import create

class MyMainWindow(QMainWindow, Ui_MainWindow, Changer, create):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createProject.clicked.connect(self.onCreateProjectClicked)
        self.deleteItem.clicked.connect(self.DeleteItem)
        self.db = TinyDB("data.json")
        self.loadList()
        self.langSelect.currentIndexChanged.connect(self.updateLibarySettings)
        self.listWidget.itemClicked.connect(self.listClicked)
        self.listWidget.itemClicked
        self.searchBar.textChanged.connect(self.search)
        self.selectFolder.clicked.connect(self.selectWindow)
        
    
    def updateLibarySettings(self):
        selectedType = self.langSelect.currentText()
        if selectedType == "Python":
            self.PythonChanger()
        if selectedType == "Ruby":
            self.RubyChanger()
        if selectedType == "C#":
            self.CsharpChanger()
        if selectedType == "Rust":
            self.rustChanger()
        if selectedType == "Lua":
            self.luaChanger()
        if selectedType == "Web":
            self.WebChanger()
    
    def onCreateProjectClicked(self):
        projectName = self.projectNamer.text()
        Directory = self.directoryAssign.text()

        if not projectName:
            QMessageBox.critical(self, "Error", "Please Enter Project Name")
            return

        selectedType = self.langSelect.currentText()
        selectedLibary = self.libarySelect.currentText()
        if selectedType == "Python":
            if selectedLibary == "Flask":
                self.Python(projectName, pyPath=Directory, Current="Flask")
            elif selectedLibary == "PyGame":
                self.Python(projectName, pyPath=Directory, Current="PyGame")
            elif selectedLibary == "Django":
                self.Python(projectName, pyPath=Directory, Current="Django")
            else:
                self.Python(projectName, pyPath=Directory, Current="None")
        if selectedType == "C#":
            
            if selectedLibary == "Console":
                self.CSharp(projectName, csPath=Directory, current="Console")
            elif selectedLibary == "WPF":
                self.CSharp(projectName, csPath=Directory, current="WPF")
        elif selectedType == "Ruby":
            if selectedLibary == "Gosu":
                self.Ruby(projectName, rbPath=Directory, Current="Gosu")
            else:
                self.Ruby(projectName, rbPath=Directory, Current="None")
        elif selectedType == "Web":
            self.Web(projectName, webPath=Directory)
        elif selectedType == "Rust":
            self.Rust(projectName, rsPath=Directory, Current="None")
        elif selectedType == "Lua":
            self.Lua(projectName, luaPath=Directory, Current="None")
        self.loadList()

    def selectWindow(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        self.directoryAssign.setText(fname)
        
    def loadList(self):
        self.listWidget.clear()
        inList = self.db.all()
        for List in inList:
            self.listWidget.addItem(List["Name"])

        font = self.listWidget.font()
        font.setPointSize(20)  # Change the number to adjust font size
        self.listWidget.setFont(font)
    def listClicked(self, item):
        projectName = item.text()
        projectInfo = self.db.get(Query().Name == projectName)
        if projectInfo:
            projectDirectory = projectInfo["Directory"]
            os.startfile(projectDirectory)
            vscodeCommand = "code {}".format(projectDirectory)
            subprocess.run(vscodeCommand, shell=True)

    def DeleteItem(self):
        try:
            current_item = self.listWidget.currentItem()
            if current_item:
                name = current_item.text()
                material = self.db.get(Query().Name == name)
                if material:
                    itemDir = material["Directory"]  # Retrieve the directory path
                    shutil.rmtree(itemDir)  # Delete the directory and its contents
                    self.db.remove(doc_ids=[material.doc_id])
                
            else:
                QMessageBox.warning(self, "Warning", "Item not selected")

            self.listWidget.clear()
            inList = self.db.all()
            for List in inList:
                self.listWidget.addItem(List["Name"])
        except:
            QMessageBox.warning(self, "Warning", "This Project Was Opened Please Close Project First")

    def search(self):
        keyword = self.searchBar.text().strip()
        if keyword:
            results = self.db.search(
                (Query().Name.search(keyword)) |
                (Query().Directory.search(keyword))
            )
            self.searchItems(results)
        else:
            self.loadList()
    def searchItems(self, results):
        self.listWidget.clear()
        for data in results:
            list_item = QListWidgetItem(data["Name"])
            self.listWidget.addItem(list_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())