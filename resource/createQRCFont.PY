import sys
import os

PREFIX = "/"


def searchFile(root, result):
    for file in os.listdir(root):
        fullpath = os.path.join(root, file)

        if os.path.isdir(fullpath):
            searchFile(fullpath, result)

        if file.split('.')[-1] == "ttf":
            result.append(fullpath)
    return result


def main():
    root = sys.argv[1]
    root = os.path.join(root, "resource")
    files = searchFile(root, [])
    qrc = os.path.join(root, r"fontResource.qrc")
    fw = open(qrc, 'w')
    fw.write('<RCC>\n')
    fw.write('  <qresource prefix="%s">\n' % PREFIX)
    for file in files:
        print(file)
        file = file.replace(root, './')
        fw.write('    <file>%s</file>\n' % file)
    fw.write('  </qresource>\n')
    fw.write('</RCC>\n')
    print(fw)


if __name__ == '__main__':
    main()
