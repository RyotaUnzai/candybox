# Python標準
import os
import codecs
import json
import glob
import logging


def getBasename(path, ext=True):
    u"""
    パス文字列からファイル名（ディレクトリ名）を返す
    """
    if ext is True:
        basename = os.path.basename(path)
    else:
        basename = os.path.splitext(os.path.basename(path))[0]
    return basename


def getDirname(path):
    u"""
    パス文字列からフォルダ名（ディレクトリ名）を返す
    """
    dirname = os.path.dirname(path)
    return dirname


def getSubdirname(path):
    u"""
    ファイルの直上のフォルダ名を返す
    """
    subdirname = os.path.basename(os.path.dirname(path))
    return subdirname


def existsMakeDirs(path):
    u"""
    pathが存在しない場合ディレクトリを作成する
    """
    if not os.path.exists(path):
        os.makedirs(path)


def sortOnlyFilelist(path):
    u"""
    ファイル名のみの一覧をlistで返す
    :return: OnlyDirlist
    """
    files = os.listdir(path)
    sortOnlyFilelist = [f for f in files if os.path.isfile(os.path.join(path, f))]
    return sortOnlyFilelist


def sortOnlyDirlist(path):
    u"""
    ディレクトリ名のみの一覧をlistで返す
    :return: OnlyDirlist
    """
    files = os.listdir(path)
    OnlyDirlist = [f for f in files if os.path.isdir(os.path.join(path, f))]
    return OnlyDirlist


def loadJson(path, decoding="utf-8-sig"):
    u"""
    jsonをloadする
    指定しなければutf-8-sigでdecodingする
    :param path: jsonPath
    :param decoding: set decoding
    :return: jsonTxt
    """
    text = ""
    with open(path) as file:
        try:
            text = json.load(file)
        except ValueError:
            try:
                text = json.load(codecs.open(file, "r", decoding))
            except TypeError:
                text = json.loads(open(path).read().decode(decoding))
    return text


def readFile(path, decoding="utf-8-sig"):
    u"""
    fileをreadする
    指定しなければutf-8-sigでdecodingする
    :param path: jsonPath
    :param decoding: set decoding
    :return: jsonTxt
    """
    text = ""
    with open(path) as file:
        try:
            text = file.read()
        except ValueError:
            try:
                text = codecs.open(file, "r", decoding)
            except TypeError:
                try:
                    text = open(path).read().decode(decoding)
                except UnicodeDecodeError:
                    text = open(path).read().decode("utf-8_sig")
    return text



def saveFile(path, data):
    with open(path, mode='w') as f:
        f.write(data)


def dict2json(data):
    """
    dictをjsonにdumpする
    :return: json
    """
    return json.dumps(data, indent=4)


def saveJson(path, data):
    u"""
    jsonをsaveする
    :param path: jsonPath
    :param data: jsonData
    """
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.debug(path)


def existsMakeJson(path, data):
    if not os.path.exists(path):
        saveJson(path, data)


def refreshPath(path, values=[]):
    u"""
    pathとvaluesを結合したpathを作成する
    :param path:
    :param values: string or list
    :return: os.path.join(newPath, values)
    """
    newPath = path
    if values == []:
        pass
    elif isinstance(values, list):
        for value in values:
            newPath = os.path.join(newPath, value)
    else:
        newPath = os.path.join(newPath, values)
    newPath = newPath.replace("\\", "/")
    return newPath


def addDictKey(string, dict, value=None):
    """
    dictのkeysにkeyが存在していない場合はstringのkeyを作成する
    :param string:
    :param dict:
    :return: dict[string] = {}
    """
    if string not in dict:
        if value is not None:
            dict[string] = value
        else:
            dict[string] = {}

        return dict
    return dict


def checkDir(path):
    u"""
    pathが存在していないばあいディレクトリを作成する

    :param if not os.path.exists(path): os.mkdir(path)
    """
    if not os.path.exists(path):
        os.mkdir(path)


def checkJsonFile(path):
    u"""
    pathが存在していないばあいディレクトリを作成する

    :param if not os.path.exists(path): os.mkdir(path)
    """
    if not os.path.exists(path):
        saveJson(path, {})


def getExtList(path="", ext=".json"):
    u"""
    """
    files = glob.glob("%s/**/*" % path)
    return [file.replace("\\", "/") for file in files if os.path.splitext(file)[1] == ext]


def isInt(s):
    """[summary]
    s is Int or isn't
    Args:
        s ([type]): [description]

    Returns:
        [type]: [description]
    """

    try:
        int(s)
        return True
    except ValueError:
        return False


def existsMakeFile(path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass
