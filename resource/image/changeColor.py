import sys
import os

PREFIX = "/"

color = "#fff"
# color = "#6e6d72"  # default
# color = "#ededed"  # hover
root = os.path.dirname(os.path.abspath(sys.argv[0]))
lightRoot = os.path.join(root, "light")


def searchFile(root, result):
    for file in os.listdir(root):
        fullpath = os.path.join(root, file)

        if os.path.isdir(fullpath):
            searchFile(fullpath, result)

        if file.split('.')[-1] == "svg":
            result.append(fullpath)
    return result


files = searchFile(lightRoot, [])
for file in files:
    with open(file, "r") as f:
        data = ""
        for line in f:
            fixLine = line
            if "<path d=" in fixLine:
                fixLine = fixLine.replace("<path d=", '<path fill="%s" d=' % color)
            data += fixLine
    with open(file, "w") as f:
        f.write(data)
