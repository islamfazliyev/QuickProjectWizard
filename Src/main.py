import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidgetItem, QPushButton, QMessageBox, QComboBox
from uiV5 import Ui_MainWindow
from tinydb import TinyDB, Query
import subprocess
import shutil
from LibaryChanger import Changer

class MyMainWindow(QMainWindow, Ui_MainWindow, Changer):
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
            self.CSharp(projectName, csPath=Directory, current="None")
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
        self.loadList()

    def selectWindow(self):
        fname = str(QFileDialog.getExistingDirectoryUrl(self, "Select Folder"))
        unwantedTexts = "'"
        fname.translate("", "", unwantedTexts)
        self.directoryAssign.setText(fname[27:])
        
    def Python(self, path, pyPath, Current):
        directory = os.path.join(f"{pyPath}", path)
        os.mkdir(directory)
        pyFile = os.path.join(directory, "main.py")
        os.startfile(directory)
        with open(pyFile, "w") as fp:
            if Current == "Flask":
                pyContent = """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
"""
                fp.write(pyContent)
            elif Current == "PyGame":
                pyContent = """
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Window")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()

"""
                fp.write(pyContent)

            elif Current == "None":
                pyContent = """print("Hello World!!")"""
                fp.write(pyContent)
        
        self.db.insert({
            "Name": path,
            "Directory": directory 
        })
        print("Project folder and script file created successfully.")
    def CSharp(self, path, csPath, current):
        Directory = os.path.join(f"{csPath}", path)
        os.mkdir(Directory)
        if current == "Console":
            csharpCommand = f'cd {Directory} && dotnet new console'
        elif current == "WPF":
            csharpCommand = f'cd {Directory} && dotnet new wpf'
        subprocess.run(csharpCommand, shell=True)
        os.startfile(Directory)
        self.db.insert({
            "Name": path,
            "Directory": Directory 
        })
        print("Project folder and script file created successfully.")

    def Ruby(self, path, rbPath, Current):
        Directory = os.path.join(f"{rbPath}", path)
        os.mkdir(Directory)
        global rbFile
        rbFile = os.path.join(Directory, "main.rb")
        os.startfile(rbPath)
        with open(rbFile, "w") as fp:
            if Current == "Gosu":
                rbContent = """
require 'gosu'

class GameWindow < Gosu::Window
  def initialize
    super(800, 600, false)
    self.caption = "Basic Gosu Program"
  end

  def update
    # Update logic goes here
  end

  def draw
    draw_rect(100, 100, 50, 50, Gosu::Color::RED)
  end

  private

  def draw_rect(x, y, width, height, color)
    draw_quad(x, y, color,
              x + width, y, color,
              x, y + height, color,
              x + width, y + height, color)
  end
end

window = GameWindow.new
window.show
"""
                fp.write(rbContent)
            elif Current == "None":
                rbContent = """puts("Hello World")"""
                fp.write(rbContent)
        self.db.insert({
            "Name": path,
            "Directory": rbPath
        })
        print("Project folder and script file created successfully.")
    def Web(self, path, webPath):
        Directory = os.path.join(f"{webPath}", path)
        os.mkdir(Directory)
        webFile = os.path.join(Directory, "index.html")
        os.startfile(Directory)
        self.db.insert({
            "Name": path,
            "Directory": Directory 
        })
        with open(webFile, "w") as fp:
            html_content = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>"""
            fp.write(html_content)
            pass
        Directory = os.path.join(f"{webPath}", path, "js")
        os.mkdir(Directory)
        webFile = os.path.join(Directory, "script.js")
        with open(webFile, "w") as fp:
            pass
        Directory = os.path.join(f"{webPath}", path, "css")
        os.mkdir(Directory)
        webFile = os.path.join(Directory, "style.css")
        with open(webFile, "w") as fp:
            pass
        print("Project folder and script file created successfully.")
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
            vscodeCommand = "code {}".format(projectDirectory)
            subprocess.run(vscodeCommand, shell=True)

    def DeleteItem(self):
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