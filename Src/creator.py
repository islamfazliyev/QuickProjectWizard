import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidgetItem, QPushButton, QMessageBox, QComboBox
from uiV5 import Ui_MainWindow
from tinydb import TinyDB, Query
import subprocess
import shutil

class create:
    def Python(self, path, pyPath, Current):
        Directory = os.path.join(f"{pyPath}", path)
        os.mkdir(Directory)
        Directory2 = os.chdir(f"{Directory}")
        os.mkdir("src")
        os.mkdir("assets")
        os.mkdir("docs")
        pyFile = os.path.join(f"{Directory}\\src", "main.py")
        os.startfile(Directory)
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
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
        
        self.db.insert({
            "Name": path,
            "Directory": Directory 
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
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
        self.db.insert({
            "Name": path,
            "Directory": Directory 
        })
        print("Project folder and script file created successfully.")

    def Ruby(self, path, rbPath, Current):
        Directory = os.path.join(f"{rbPath}", path)
        global rbFile
        os.mkdir(Directory)
        Directory2 = os.chdir(f"{Directory}")
        os.mkdir("src")
        os.mkdir("assets")
        os.mkdir("docs")
        rbFile = os.path.join(f"{Directory}\\src", "main.rb")
        os.startfile(Directory)
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
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
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
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
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

    def Rust(self, path, rsPath, Current):
        Directory = os.path.join(f"{rsPath}", path)
        cargoCommand = f"cargo new {path}"
        subprocess.run(cargoCommand, shell=True)
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
        self.db.insert({
            "Name": path,
            "Directory": Directory
        })
        os.startfile(Directory)
    
    def Lua(self, path, luaPath, Current):
        Directory = os.path.join(f"{luaPath}", path)
        os.mkdir(Directory)
        Directory2 = os.chdir(f"{Directory}")
        os.mkdir("src")
        os.mkdir("assets")
        os.mkdir("docs")
        luaFile = os.path.join(f"{Directory}\\src", "main.lua")
        vscodeCommand = "code {}".format(Directory)
        subprocess.run(vscodeCommand, shell=True)
        with  open(luaFile, 'w') as file:
            lua_content= """print("hello world")"""
            file.write(lua_content)
        self.db.insert({
            "Name": path,
            "Directory": Directory
        })
        os.startfile(Directory)