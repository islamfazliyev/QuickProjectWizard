import os

print("availables, python, ruby, web")
projectSelector = input("Select your project type")
folderNamer = input("Enter Project Name")


def Python():
    pyPath = os.path.join(r"D:\codes\python", folderNamer)
    os.mkdir(pyPath)
    pyFile = os.path.join(pyPath, "main.py")
    os.startfile(pyPath)
    with open(pyFile, "w") as fp:
        pyContent = """print("Hello World")"""
        fp.write(pyContent)
    print("Project folder and script file created successfully.")

def Ruby():
    rbPath = os.path.join(r"D:\codes\ruby", folderNamer)
    os.mkdir(rbPath)
    rbFile = os.path.join(rbPath, "main.rb")
    os.startfile(rbPath)
    with open(rbFile, "w") as fp:
        rbContent = """puts ("Hello World")"""
        fp.write(rbContent)
    print("Project folder and script file created successfully.")
def Web():
    webPath = os.path.join(r"D:\codes\html", folderNamer)
    os.mkdir(webPath)
    webFile = os.path.join(webPath, "index.html")
    os.startfile(webPath)
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
    webPath = os.path.join(r"D:\codes\html", folderNamer, "js")
    os.mkdir(webPath)
    webFile = os.path.join(webPath, "script.js")
    with open(webFile, "w") as fp:
        pass
    webPath = os.path.join(r"D:\codes\html", folderNamer, "css")
    os.mkdir(webPath)
    webFile = os.path.join(webPath, "style.css")
    with open(webFile, "w") as fp:
        pass
    print("Project folder and script file created successfully.")


if projectSelector == "python":
    Python()
elif projectSelector == "ruby":
    Ruby()
elif projectSelector == "web":
    Web()